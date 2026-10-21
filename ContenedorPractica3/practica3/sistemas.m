% Práctica 3 · UEA 1151039. Octave usa índices desde 1.
% octave sistemas.m casos/ejemplo.dat [lambda]
1;
function r = rr(A,b,x)
  nr=0; nb=0; n=length(b);
  for i=1:n
    ax=0; for j=1:n, ax=ax+A(i,j)*x(j); end
    nr=max(nr,abs(b(i)-ax)); nb=max(nb,abs(b(i)));
  end
  r=nr/max(nb,1e-300);
end
function v = norma2(x)
  s=0; for i=1:length(x), s=s+x(i)*x(i); end; v=sqrt(s);
end
function [M,p,ok] = factorizar(A,pivote)
  n=rows(A); M=A; p=1:n; ok=true;
  for k=1:n
    best=k;
    if pivote
      for i=k+1:n
        if abs(M(p(i),k))>abs(M(p(best),k)),best=i;end
      end
    end
    t=p(k);p(k)=p(best);p(best)=t;
    if M(p(k),k)==0 || !isfinite(M(p(k),k)),ok=false;return;end
    for i=k+1:n
      m=M(p(i),k)/M(p(k),k);M(p(i),k)=m;
      for j=k+1:n,M(p(i),j)=M(p(i),j)-m*M(p(k),j);end
    end
  end
end
function x = resolver_lu(M,p,b)
  n=length(b);y=zeros(n,1);x=zeros(n,1);
  for i=1:n
    s=0;for j=1:i-1,s=s+M(p(i),j)*y(j);end;y(i)=b(p(i))-s;
  end
  for i=n:-1:1
    s=0;for j=i+1:n,s=s+M(p(i),j)*x(j);end;x(i)=(y(i)-s)/M(p(i),i);
  end
end
function [x,ok] = cholesky_manual(A,b)
  n=length(b);L=zeros(n);y=zeros(n,1);x=zeros(n,1);ok=true;
  for i=1:n,for j=1:n,if abs(A(i,j)-A(j,i))>1e-12,ok=false;return;end;end;end
  for i=1:n
    for j=1:i
      s=0;for k=1:j-1,s=s+L(i,k)*L(j,k);end
      if i==j
        if A(i,i)-s<=0,ok=false;return;end;L(i,j)=sqrt(A(i,i)-s);
      else,L(i,j)=(A(i,j)-s)/L(j,j);end
    end
  end
  for i=1:n,s=0;for j=1:i-1,s=s+L(i,j)*y(j);end;y(i)=(b(i)-s)/L(i,i);end
  for i=n:-1:1,s=0;for j=i+1:n,s=s+L(j,i)*x(j);end;x(i)=(y(i)-s)/L(i,i);end
end
function fila(tipo,name,k,x,ea,res,estado)
  printf('%s,%s,%d',tipo,name,k);
  for i=1:length(x),printf(',%.9f',x(i));end
  printf(',%.6e,%.6e,%s\n',ea,res,estado);
end
function iterar(A,b,tipo,lambda)
  names={'Jacobi','Gauss-Seidel','SOR'};name=names{tipo+1};n=length(b);
  x=zeros(n,1);ea=0;res=rr(A,b,x);estado='MAX_ITER';
  if any(diag(A)==0),fila('RESUMEN',name,0,x,0,res,'DIAGONAL_CERO');return;end
  for k=1:200
    old=x;
    for i=1:n
      s=0;
      for j=1:n
        if i!=j
          if tipo==0 || j>i,v=old(j);else,v=x(j);end
          s=s+A(i,j)*v;
        end
      end
      nuevo=(b(i)-s)/A(i,i);
      if tipo==2,x(i)=lambda*nuevo+(1-lambda)*old(i);else,x(i)=nuevo;end
    end
    ea=100*norma2(x-old)/max(norma2(x),1e-300);res=rr(A,b,x);
    if !isfinite(ea)||!isfinite(res)||norma2(x)>1e100,estado='DIVERGE';break;end
    fila('ITER',name,k,x,ea,res,'PASO');
    if ea<=0.5&&res<=1e-6,estado='CONVERGE';break;end
  end
  fila('RESUMEN',name,k,x,ea,res,estado);
end
args=argv();file='casos/ejemplo.dat';lambda=1.1;
if length(args)>=1,file=args{1};end
if length(args)>=2,lambda=str2double(args{2});end
if !(lambda>0&&lambda<2),error('Use 0 < lambda < 2');end
fid=fopen(file,'r');if fid<0,error('No se puede abrir el archivo');end
n=fscanf(fid,'%d',1);if n<1||n>20,fclose(fid);error('Dimension fuera de rango');end
vals=fscanf(fid,'%f');fclose(fid);if length(vals)!=n*n+n,error('Formato .dat inválido');end
A=reshape(vals(1:n*n),n,n)';b=vals(n*n+1:end);
printf('tipo,metodo,k');for i=1:n,printf(',x%d',i);end;printf(',ea_pct,res_rel_inf,estado\n');
for use=0:1
  names={'Gauss-simple','Gauss-pivote'};name=names{use+1};
  [M,p,ok]=factorizar(A,use);x=zeros(n,1);estado='PIVOTE_NULO';
  if ok
    x=resolver_lu(M,p,b);estado='RESUELTO';if rr(A,b,x)>1e-6,estado='RESIDUO_ALTO';end
  end
  fila('RESUMEN',name,0,x,0,rr(A,b,x),estado);
  if use&&ok,x=resolver_lu(M,p,2*b);fila('RESUMEN','LU-2b',0,x,0,rr(A,2*b,x),'RESUELTO_2b');end
end
[x,ok]=cholesky_manual(A,b);estado='NO_APLICA';if ok,estado='RESUELTO';end
fila('RESUMEN','Cholesky',0,x,0,rr(A,b,x),estado);
for tipo=0:2,iterar(A,b,tipo,lambda);end
