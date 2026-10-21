"""Práctica 3: algoritmos explícitos y verificación independiente con NumPy.
Uso: python3 sistemas.py casos/ejemplo.dat [lambda] [--analisis]
Los bucles siguen el mismo orden aritmético que C y Octave.
"""
import sys, math, csv, json
from pathlib import Path
import numpy as np

MAXIT=200
def leer(path):
    vals=Path(path).read_text().split(); n=int(vals[0]); a=list(map(float,vals[1:]));
    if not 1<=n<=20 or len(a)!=n*n+n: raise ValueError('Formato .dat inválido')
    return [a[i*n:(i+1)*n] for i in range(n)], a[n*n:]

def norma2(x):
    s=0.0
    for v in x:s+=v*v
    return math.sqrt(s)

def residuo(A,b,x):
    nr=nb=0.0
    for row,rhs in zip(A,b):
        ax=0.0
        for a,v in zip(row,x):ax+=a*v
        nr=max(nr,abs(rhs-ax));nb=max(nb,abs(rhs))
    return nr/max(nb,1e-300)

def factorizar(A,pivote=True):
    n=len(A); M=[row[:] for row in A]; p=list(range(n))
    for k in range(n):
        best=k
        if pivote:
            for i in range(k+1,n):
                if abs(M[p[i]][k])>abs(M[p[best]][k]):best=i
        p[k],p[best]=p[best],p[k]
        if M[p[k]][k]==0 or not math.isfinite(M[p[k]][k]):return None
        for i in range(k+1,n):
            m=M[p[i]][k]/M[p[k]][k]; M[p[i]][k]=m
            for j in range(k+1,n):M[p[i]][j]-=m*M[p[k]][j]
    return M,p

def resolver_lu(fac,b):
    M,p=fac;n=len(b);y=[0.0]*n;x=[0.0]*n
    for i in range(n):
        s=0.0
        for j in range(i):s+=M[p[i]][j]*y[j]
        y[i]=b[p[i]]-s
    for i in range(n-1,-1,-1):
        s=0.0
        for j in range(i+1,n):s+=M[p[i]][j]*x[j]
        x[i]=(y[i]-s)/M[p[i]][i]
    return x

def cholesky(A,b):
    n=len(b);L=[[0.0]*n for _ in b];y=[0.0]*n;x=[0.0]*n
    if any(abs(A[i][j]-A[j][i])>1e-12 for i in range(n) for j in range(n)):return None
    for i in range(n):
        for j in range(i+1):
            s=0.0
            for k in range(j):s+=L[i][k]*L[j][k]
            if i==j:
                if A[i][i]-s<=0:return None
                L[i][j]=math.sqrt(A[i][i]-s)
            else:L[i][j]=(A[i][j]-s)/L[j][j]
    for i in range(n):
        s=0.0
        for j in range(i):s+=L[i][j]*y[j]
        y[i]=(b[i]-s)/L[i][i]
    for i in range(n-1,-1,-1):
        s=0.0
        for j in range(i+1,n):s+=L[j][i]*x[j]
        x[i]=(y[i]-s)/L[i][i]
    return x

def iterar(A,b,tipo,lam=1.1,maxit=MAXIT):
    n=len(b); x=[0.0]*n; rows=[]; rr=residuo(A,b,x)
    if any(A[i][i]==0 for i in range(n)):return x,0,0.0,rr,'DIAGONAL_CERO',rows
    estado='MAX_ITER';ea=0.0
    for k in range(1,maxit+1):
        old=x[:]
        for i in range(n):
            s=0.0
            for j in range(n):
                if i!=j:s+=A[i][j]*(old[j] if tipo==0 or j>i else x[j])
            nuevo=(b[i]-s)/A[i][i]
            x[i]=lam*nuevo+(1-lam)*old[i] if tipo==2 else nuevo
        ea=100*norma2([v-w for v,w in zip(x,old)])/max(norma2(x),1e-300)
        rr=residuo(A,b,x)
        if not math.isfinite(ea) or not math.isfinite(rr) or norma2(x)>1e100:
            estado='DIVERGE';break
        rows.append((k,x[:],ea,rr))
        if ea<=0.5 and rr<=1e-6:estado='CONVERGE';break
    return x,k,ea,rr,estado,rows

def fila(tipo,name,k,x,ea,rr,estado):
    return ','.join([tipo,name,str(k)]+[f'{v:.9f}' for v in x]+[f'{ea:.6e}',f'{rr:.6e}',estado])

def ejecutar(A,b,lam=1.1):
    n=len(b);lines=[','.join(['tipo','metodo','k']+[f'x{i+1}' for i in range(n)]+['ea_pct','res_rel_inf','estado'])]
    for use,name in [(False,'Gauss-simple'),(True,'Gauss-pivote')]:
        fac=factorizar(A,use); x=resolver_lu(fac,b) if fac else [0.0]*n;rr=residuo(A,b,x)
        status=('RESUELTO' if rr<=1e-6 else 'RESIDUO_ALTO') if fac else 'PIVOTE_NULO'
        lines.append(fila('RESUMEN',name,0,x,0.0,rr,status))
        if use and fac:
            b2=[2*v for v in b];x=resolver_lu(fac,b2)
            lines.append(fila('RESUMEN','LU-2b',0,x,0.0,residuo(A,b2,x),'RESUELTO_2b'))
    x=cholesky(A,b);ok=x is not None;x=x if ok else [0.0]*n
    lines.append(fila('RESUMEN','Cholesky',0,x,0.0,residuo(A,b,x),'RESUELTO' if ok else 'NO_APLICA'))
    for tipo,name in enumerate(['Jacobi','Gauss-Seidel','SOR']):
        x,k,ea,rr,status,rows=iterar(A,b,tipo,lam)
        for j,v,e,r in rows:lines.append(fila('ITER',name,j,v,e,r,'PASO'))
        lines.append(fila('RESUMEN',name,k,x,ea,rr,status))
    return '\n'.join(lines)+'\n'

def analizar(A,b,lam=1.1):
    a=np.array(A);bb=np.array(b);n=len(b)
    rankA=int(np.linalg.matrix_rank(a));rankAb=int(np.linalg.matrix_rank(np.column_stack([a,bb])))
    classification='única' if rankA==n else ('incompatible' if rankAb>rankA else 'infinitas')
    if rankA<n:return dict(tipo=classification,rango_A=rankA,rango_Ab=rankAb)
    ref=np.linalg.solve(a,bb)
    diag=np.abs(np.diag(a));others=np.sum(np.abs(a),axis=1)-diag
    D=np.diag(np.diag(a));L=np.tril(a,-1);U=np.triu(a,1)
    radii={}
    if np.all(np.diag(a)!=0):
        for name,T in [('Jacobi',np.linalg.solve(D,-L-U)),('Gauss-Seidel',np.linalg.solve(D+L,-U)),('SOR',np.linalg.solve(D+lam*L,(1-lam)*D-lam*U))]:
            radii[name]=float(max(abs(np.linalg.eigvals(T))))
    cond=float(np.linalg.cond(a,np.inf));inv=np.linalg.inv(a)
    perturb=bb.copy();perturb[-1]+=1e-6*max(abs(bb))
    shifted=np.linalg.solve(a,perturb)
    relb=float(np.linalg.norm(perturb-bb,np.inf)/np.linalg.norm(bb,np.inf))
    relx=float(np.linalg.norm(shifted-ref,np.inf)/np.linalg.norm(ref,np.inf))
    try:np.linalg.cholesky(a);spd=bool(np.allclose(a,a.T,rtol=0,atol=1e-12))
    except np.linalg.LinAlgError:spd=False
    fac=factorizar(A,True);M,p=fac;lu=np.array([M[i] for i in p]);low=np.tril(lu,-1)+np.eye(n);up=np.triu(lu);P=np.eye(n)[p]
    sweep=[]
    for w in np.arange(.2,1.91,.05):
        x,k,ea,rr,status,_=iterar(A,b,2,float(w));sweep.append(dict(lam=round(float(w),2),k=k,estado=status,res=rr))
    valid=[s for s in sweep if s['estado']=='CONVERGE'];best=min(valid,key=lambda s:(s['k'],abs(s['lam']-1))) if valid else None
    traces={}
    for typ,name in enumerate(['Jacobi','Gauss-Seidel','SOR']):
        x,k,ea,rr,status,rows=iterar(A,b,typ,lam)
        traces[name]=dict(x=x,k=k,ea=ea,res=rr,estado=status,
                         error_verdadero_pct=float(100*np.linalg.norm(np.array(x)-ref,np.inf)/np.linalg.norm(ref,np.inf)),
                         filas=[dict(k=j,x=v,ea=e,res=r) for j,v,e,r in rows])
    return dict(tipo=classification,rango_A=rankA,rango_Ab=rankAb,x_ref=ref.tolist(),
                cond_inf=cond,dominante=bool(np.all(diag>others)),margen_diagonal=(diag-others).tolist(),
                spd=spd,rho=radii,res_lu=float(np.linalg.norm(P@a-low@up,np.inf)/np.linalg.norm(a,np.inf)),
                P=P.tolist(),L=low.tolist(),U=up.tolist(),
                error_inv=float(np.linalg.norm(inv@bb-ref,np.inf)),
                perturbacion=dict(rel_b=relb,rel_x=relx,cota=cond*relb),
                barrido=sweep,mejor_lambda=best,iterativos=traces)

def graficar(info,out):
    print('graficar(): falta completar; ver COMO_CORRER.md')

def main():
    args=[s for s in sys.argv[1:] if not s.startswith('--')]
    file=args[0] if args else 'casos/ejemplo.dat';lam=float(args[1]) if len(args)>1 else 1.1
    if not 0<lam<2:raise ValueError('Use 0 < lambda < 2')
    A,b=leer(file);print(ejecutar(A,b,lam),end='')
    if '--analisis' in sys.argv:
        info=analizar(A,b,lam);stem=Path(file).stem;out=Path('resultados')/stem;out.mkdir(parents=True,exist_ok=True)
        (out/'analisis.json').write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf-8')
        print('ANALISIS',json.dumps({k:v for k,v in info.items() if k in ['tipo','x_ref','cond_inf','dominante','spd','rho','mejor_lambda']},ensure_ascii=False))
        if info['tipo']=='única':graficar(info,out/'img')

if __name__=='__main__':main()
