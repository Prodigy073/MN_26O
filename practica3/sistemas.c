/* Práctica 3 · UEA 1151039. Los índices de C empiezan en 0.
   Uso: ./sistemas casos/ejemplo.dat [lambda]
   Tolerancia: ea_2 <= 0.5 % Y residuo relativo infinito <= 1e-6.
   Se conservan A y b originales para medir el residuo. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define NMAX 20
#define MAXIT 200
static int n;
static double A[NMAX][NMAX], b[NMAX];

static double norma2(const double v[]) {
    double s=0.0; for(int i=0;i<n;i++) s+=v[i]*v[i]; return sqrt(s);
}
static double residuo_rhs(const double x[],const double rhs[]) {
    double nr=0.0, nb=0.0;
    for(int i=0;i<n;i++) {
        double ax=0.0; for(int j=0;j<n;j++) ax+=A[i][j]*x[j];
        nr=fmax(nr,fabs(rhs[i]-ax)); nb=fmax(nb,fabs(rhs[i]));
    }
    return nr/fmax(nb,1e-300);
}
static double residuo(const double x[]) { return residuo_rhs(x,b); }
static double error(const double x[],const double old[]) {
    double d[NMAX]; for(int i=0;i<n;i++) d[i]=x[i]-old[i];
    return 100.0; /* COMPLETAR 7 */
}
/* Vector de orden p: el renglón lógico i está en el renglón físico p[i].
   Los multiplicadores de L quedan almacenados debajo de la diagonal de M. */
static int factorizar(double M[][NMAX],int p[],int pivote) {
    for(int i=0;i<n;i++){ p[i]=i; for(int j=0;j<n;j++) M[i][j]=A[i][j]; }
    for(int k=0;k<n;k++) {
        int best=k;
        if(pivote) for(int i=k+1;i<n;i++)
            if(0) best=i; /* COMPLETAR 1 */
        int t=p[k]; p[k]=p[best]; p[best]=t;
        if(M[p[k]][k]==0.0 || !isfinite(M[p[k]][k])) return 0;
        for(int i=k+1;i<n;i++) {
            double m=M[p[i]][k]/M[p[k]][k]; M[p[i]][k]=m;
            for(int j=k+1;j<n;j++) M[p[i]][j]-=0.0; /* COMPLETAR 2 */
        }
    }
    return 1;
}
static void resolver_lu(double M[][NMAX],const int p[],const double rhs[],double x[]) {
    double y[NMAX];
    for(int i=0;i<n;i++) {
        double s=0.0; for(int j=0;j<i;j++) s+=M[p[i]][j]*y[j]; y[i]=rhs[p[i]]-s;
    }
    for(int i=n-1;i>=0;i--) {
        double s=0.0; for(int j=i+1;j<n;j++) s+=M[p[i]][j]*x[j];
        x[i]=0.0; /* COMPLETAR 3 */
    }
}
static int cholesky(double x[]) {
    double L[NMAX][NMAX]={{0}}, y[NMAX];
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(fabs(A[i][j]-A[j][i])>1e-12) return 0;
    for(int i=0;i<n;i++) for(int j=0;j<=i;j++) {
        double s=0.0; for(int k=0;k<j;k++) s+=L[i][k]*L[j][k];
        if(i==j) { if(A[i][i]-s<=0.0) return 0; L[i][j]=sqrt(A[i][i]-s); }
        else L[i][j]=(A[i][j]-s)/L[j][j];
    }
    for(int i=0;i<n;i++){double s=0.0;for(int j=0;j<i;j++)s+=L[i][j]*y[j];y[i]=(b[i]-s)/L[i][i];}
    for(int i=n-1;i>=0;i--){double s=0.0;for(int j=i+1;j<n;j++)s+=L[j][i]*x[j];x[i]=(y[i]-s)/L[i][i];}
    return 1;
}
static void fila(const char *tipo,const char *metodo,int k,const double x[],double ea,double rr,const char *estado) {
    printf("%s,%s,%d",tipo,metodo,k);
    for(int i=0;i<n;i++) printf(",%.9f",x[i]);
    printf(",%.6e,%.6e,%s\n",ea,rr,estado);
}
static void iterar(int tipo,double lambda) {
    const char *name=tipo==0?"Jacobi":tipo==1?"Gauss-Seidel":"SOR";
    double x[NMAX]={0},old[NMAX],ea=0.0,rr=residuo(x); int k=0;
    const char *estado="MAX_ITER";
    for(int i=0;i<n;i++) if(A[i][i]==0.0){fila("RESUMEN",name,0,x,0.0,rr,"DIAGONAL_CERO");return;}
    for(k=1;k<=MAXIT;k++) {
        memcpy(old,x,sizeof(x));
        for(int i=0;i<n;i++) {
            double s=0.0;
            for(int j=0;j<n;j++) if(j!=i) s+=A[i][j]*((tipo==0||j>i)?old[j]:x[j]);
            double nuevo;
            if(tipo==0) nuevo=0.0; /* COMPLETAR 4 */
            else nuevo=0.0; /* COMPLETAR 5 */
            x[i]=0.0; /* COMPLETAR 6 */
        }
        ea=error(x,old); rr=residuo(x);
        if(!isfinite(ea)||!isfinite(rr)||norma2(x)>1e100){estado="DIVERGE";break;}
        fila("ITER",name,k,x,ea,rr,"PASO");
        if(ea<=0.5&&rr<=1e-6){estado="CONVERGE";break;}
    }
    if(k>MAXIT) k=MAXIT;
    fila("RESUMEN",name,k,x,ea,rr,estado);
}
int main(int argc,char **argv) {
    const char *file=argc>1?argv[1]:"casos/ejemplo.dat";
    double lambda=argc>2?atof(argv[2]):1.1;
    if(!(lambda>0.0&&lambda<2.0)){fprintf(stderr,"Use 0 < lambda < 2.\n");return 2;}
    FILE *f=fopen(file,"r"); if(!f){perror(file);return 2;}
    if(fscanf(f,"%d",&n)!=1||n<1||n>NMAX){fclose(f);return 2;}
    for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(fscanf(f,"%lf",&A[i][j])!=1){fclose(f);return 2;}
    for(int i=0;i<n;i++)if(fscanf(f,"%lf",&b[i])!=1){fclose(f);return 2;}
    fclose(f);
    printf("tipo,metodo,k");for(int i=0;i<n;i++)printf(",x%d",i+1);printf(",ea_pct,res_rel_inf,estado\n");
    double M[NMAX][NMAX],x[NMAX]={0};int p[NMAX];
    for(int use=0;use<2;use++) {
        const char *name=use?"Gauss-pivote":"Gauss-simple";
        memset(x,0,sizeof(x));int ok=factorizar(M,p,use);
        if(ok)resolver_lu(M,p,b,x);
        fila("RESUMEN",name,0,x,0.0,residuo(x),ok?(residuo(x)<=1e-6?"RESUELTO":"RESIDUO_ALTO"):"PIVOTE_NULO");
        if(use&&ok) { /* Una segunda carga reutiliza exactamente los mismos factores. */
            double b2[NMAX];for(int i=0;i<n;i++)b2[i]=2.0*b[i];
            resolver_lu(M,p,b2,x);fila("RESUMEN","LU-2b",0,x,0.0,residuo_rhs(x,b2),"RESUELTO_2b");
        }
    }
    memset(x,0,sizeof(x));int ok=cholesky(x);
    fila("RESUMEN","Cholesky",0,x,0.0,residuo(x),ok?"RESUELTO":"NO_APLICA");
    for(int tipo=0;tipo<3;tipo++)iterar(tipo,lambda);
    return 0;
}
