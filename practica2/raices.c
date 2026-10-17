/* raices.c — Práctica 2: raíces de ecuaciones no lineales, en C.
 *
 * Los cinco métodos de la unidad II sobre la misma ecuación. Imprime una
 * tabla por método y un resumen; las tablas deben coincidir, cifra por cifra,
 * con las de raices.m, raices.py y las de las láminas.
 *
 * UEA 1151039 · Métodos Numéricos en Ingeniería · UAM Azcapotzalco · 26-O
 *
 * Dentro del contenedor, en la carpeta practica2:
 *     gcc -O2 -std=c17 -Wall -o raices raices.c -lm
 *     ./raices
 *
 * Faltan cinco líneas, marcadas COMPLETAR 1 a COMPLETAR 5. Mientras falten,
 * el programa compila y corre, pero las tablas salen mal.
 */
#include <math.h>
#include <stdio.h>

/* ======================== BLOQUE DEL PROBLEMA ======================== */
/* Ecuación 22 · Mecánica · Mecanismo de cuatro barras: ángulo del balancín (Freudenstein) */

#define DESCRIPCION "f(t4) = d/a cos(t4) - d/c cos(t2) + (a^2 - b^2 + c^2 + d^2)/(2 a c) - cos(t2 - t4),  a = 40, b = 120, c = 80, d = 100, t2 = 60 grados"
#define DESCR_G     "g(t4) = t4 + f(t4) / 2"

static const double LA = 40.0;   /* manivela, mm */
static const double LB = 120.0;   /* acoplador, mm */
static const double LC = 80.0;   /* balancín, mm */
static const double LD = 100.0;   /* bancada, mm */
static const double TH2 = 1.0471975511965976;   /* ángulo de la manivela, rad (60 grados) */

static const double A = 0.5, B = 1.5;  /* intervalo de los métodos cerrados */
static const double X0    = 1.0;        /* inicio de los métodos abiertos    */
static const double DELTA = 0.01;        /* incremento de la secante modificada */
static const double TOL   = 0.5;         /* tolerancia: ea en %               */
#define NMAX 50                          /* máximo de iteraciones             */

static double f(double x)
{
    return LD/LA*cos(x) - LD/LC*cos(TH2) + (LA*LA - LB*LB + LC*LC + LD*LD)/(2*LA*LC) - cos(TH2 - x);
}

/* Su derivada, para Newton-Raphson. */
static double fp(double x)
{
    return -LD/LA*sin(x) - sin(TH2 - x);
}

/* Despeje x = g(x) para punto fijo. */
static double g(double x)
{
    return x + f(x)/2;
}

/* ===================================================================== */

#define ENC_CERRADO "   k             a             b             x            f(x)     ea (%)"
#define ENC_ABIERTO "   k             x            f(x)     ea (%)"
#define ENC_RESUMEN "            x  iter.     ea (%)            f(x)   método"

typedef struct {
    double x;       /* última aproximación            */
    double ea;      /* su error aproximado, en %      */
    int    k;       /* iteraciones realizadas         */
    int    ok;      /* 1 si se alcanzó la tolerancia  */
} Resultado;

/* Error relativo aproximado, en porcentaje: |(nuevo - anterior) / nuevo| · 100. */
static double error_aprox(double nuevo, double anterior)
{
    /* COMPLETAR 1. Ojo: en C, abs() es para enteros; para double se usa fabs(). */
    return fabs((nuevo - anterior)/ nuevo) * 100;   /* <- sustituya 0.0 por la expresión correcta */
}

static void fila_cerrado(int k, double a, double b, double x, double ea, int con_ea)
{
    printf("%4d %13.6f %13.6f %13.6f %15.6e ", k, a, b, x, f(x));
    if (con_ea) printf("%10.4f\n", ea);
    else        printf("%10s\n", "-");
}

static void fila_abierto(int k, double x, double ea, int con_ea)
{
    printf("%4d %13.6f %15.6e ", k, x, f(x));
    if (con_ea) printf("%10.4f\n", ea);
    else        printf("%10s\n", "-");
}

static void cierre(Resultado r)
{
    if (r.ok)
        printf("   Raíz aproximada: %.6f  (%d iteraciones, ea = %.4f %%)\n", r.x, r.k, r.ea);
    else
        printf("   No alcanzó la tolerancia en %d iteraciones.\n", NMAX);
    printf("\n");
}

/* Bisección: parte el intervalo a la mitad y conserva la mitad con cambio de signo.
 * Este método está completo: sirve de modelo para los otros cuatro. */
static Resultado biseccion(double a, double b)
{
    Resultado r = {0.0, 0.0, 0, 0};
    double x, x_ant = 0.0, ea = 0.0;

    printf("1. Bisección en [%g, %g]\n", a, b);
    printf("%s\n", ENC_CERRADO);
    for (int k = 1; k <= NMAX; ++k) {
        x = (a + b) / 2.0;                          /* punto medio */
        if (k > 1) ea = error_aprox(x, x_ant);
        fila_cerrado(k, a, b, x, ea, k > 1);
        r.x = x; r.ea = ea; r.k = k;
        if (k > 1 && ea <= TOL) { r.ok = 1; break; }
        if (f(a) * f(x) < 0.0) b = x;               /* la raíz está en [a, x] */
        else                   a = x;               /* la raíz está en [x, b] */
        x_ant = x;
    }
    cierre(r);
    return r;
}

/* Falsa posición: corta la recta que une (a, f(a)) y (b, f(b)) con el eje x. */
static Resultado falsa_posicion(double a, double b)
{
    Resultado r = {0.0, 0.0, 0, 0};
    double x, x_ant = 0.0, ea = 0.0;

    printf("2. Falsa posición en [%g, %g]\n", a, b);
    printf("%s\n", ENC_CERRADO);
    for (int k = 1; k <= NMAX; ++k) {
        /* COMPLETAR 2: el punto donde la recta corta el eje x. */
        x = b - f(b) * (a - b) / (f(a) - f(b));   /* <- sustituya 0.0 por la expresión correcta */
        if (k > 1) ea = error_aprox(x, x_ant);
        fila_cerrado(k, a, b, x, ea, k > 1);
        r.x = x; r.ea = ea; r.k = k;
        if (k > 1 && ea <= TOL) { r.ok = 1; break; }
        if (f(a) * f(x) < 0.0) b = x;
        else                   a = x;
        x_ant = x;
    }
    cierre(r);
    return r;
}

/* Punto fijo: repite x <- g(x). */
static Resultado punto_fijo(double x)
{
    Resultado r = {x, 0.0, 0, 0};
    double x_nuevo, ea;

    printf("3. Punto fijo desde x0 = %g, con %s\n", x, DESCR_G);
    printf("%s\n", ENC_ABIERTO);
    fila_abierto(0, x, 0.0, 0);
    for (int k = 1; k <= NMAX; ++k) {
        /* COMPLETAR 3: la siguiente aproximación. */
        x_nuevo = g(x);   /* <- sustituya 0.0 por la expresión correcta */
        ea = error_aprox(x_nuevo, x);
        x = x_nuevo;
        fila_abierto(k, x, ea, 1);
        r.x = x; r.ea = ea; r.k = k;
        if (ea <= TOL) { r.ok = 1; break; }
    }
    cierre(r);
    return r;
}

/* Newton-Raphson: el cero de la recta tangente en x. */
static Resultado newton(double x)
{
    Resultado r = {x, 0.0, 0, 0};
    double x_nuevo, ea;

    printf("4. Newton-Raphson desde x0 = %g\n", x);
    printf("%s\n", ENC_ABIERTO);
    fila_abierto(0, x, 0.0, 0);
    for (int k = 1; k <= NMAX; ++k) {
        /* COMPLETAR 4: la fórmula de Newton-Raphson, con f y fp. */
        x_nuevo =  x - f(x) / fp(x);   /* <- sustituya 0.0 por la expresión correcta */
        ea = error_aprox(x_nuevo, x);
        x = x_nuevo;
        fila_abierto(k, x, ea, 1);
        r.x = x; r.ea = ea; r.k = k;
        if (ea <= TOL) { r.ok = 1; break; }
    }
    cierre(r);
    return r;
}

/* Secante modificada: Newton con la derivada aproximada por una diferencia. */
static Resultado secante_modificada(double x, double delta)
{
    Resultado r = {x, 0.0, 0, 0};
    double x_nuevo, ea;

    printf("5. Secante modificada desde x0 = %g, delta = %g\n", x, delta);
    printf("%s\n", ENC_ABIERTO);
    fila_abierto(0, x, 0.0, 0);
    for (int k = 1; k <= NMAX; ++k) {
        /* COMPLETAR 5: la pendiente es (f(x + delta) - f(x)) / delta. */
        x_nuevo =  x - delta * f(x) / (f(x + delta) - f(x));   /* <- sustituya 0.0 por la expresión correcta */
        ea = error_aprox(x_nuevo, x);
        x = x_nuevo;
        fila_abierto(k, x, ea, 1);
        r.x = x; r.ea = ea; r.k = k;
        if (ea <= TOL) { r.ok = 1; break; }
    }
    cierre(r);
    return r;
}

int main(void)
{
    const char *nombres[5] = {"Bisección", "Falsa posición", "Punto fijo",
                              "Newton-Raphson", "Secante modificada"};
    Resultado r[5];

    printf("Práctica 2 · Raíces de ecuaciones no lineales · C\n");
    printf("%s\n", DESCRIPCION);
    printf("Tolerancia: ea <= %g %%, máximo %d iteraciones\n\n", TOL, NMAX);

    r[0] = biseccion(A, B);
    r[1] = falsa_posicion(A, B);
    r[2] = punto_fijo(X0);
    r[3] = newton(X0);
    r[4] = secante_modificada(X0, DELTA);

    printf("Resumen\n");
    printf("%s\n", ENC_RESUMEN);
    for (int i = 0; i < 5; ++i)
        printf("%13.6f %6d %10.4f %15.6e   %s%s\n", r[i].x, r[i].k, r[i].ea,
               f(r[i].x), nombres[i], r[i].ok ? "" : " (no convergió)");
    return 0;
}
