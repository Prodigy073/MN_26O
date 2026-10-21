#!/usr/bin/env python3
"""raices.py — Práctica 2: raíces de ecuaciones no lineales, en Python.

Los cinco métodos de la unidad II sobre la misma ecuación. Imprime una tabla
por método y un resumen; las tablas deben coincidir, cifra por cifra, con las
de raices.m, raices.c y las de las láminas.

Python es la herramienta de verificación del curso: al final compara contra
scipy.optimize.brentq y genera las gráficas. Las gráficas faltan:
complete la función graficar().

UEA 1151039 · Métodos Numéricos en Ingeniería · UAM Azcapotzalco · 26-O

Dentro del contenedor, en la carpeta practica2:
    python3 raices.py
"""
import math
import os

import matplotlib
matplotlib.use("Agg")                    # figuras a archivo, no a ventana
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# ======================== BLOQUE DEL PROBLEMA ========================
# Ecuación 22 · Mecánica · Mecanismo de cuatro barras: ángulo del balancín (Freudenstein)

DESCRIPCION = 'f(t4) = d/a cos(t4) - d/c cos(t2) + (a^2 - b^2 + c^2 + d^2)/(2 a c) - cos(t2 - t4),  a = 40, b = 120, c = 80, d = 100, t2 = 60 grados'
DESCR_G = 'g(t4) = t4 + f(t4) / 2'

<<<<<<< Updated upstream
LA = 40.0   # manivela, mm
LB = 120.0   # acoplador, mm
LC = 80.0   # balancín, mm
LD = 100.0   # bancada, mm
TH2 = 1.0471975511965976   # ángulo de la manivela, rad (60 grados)
=======
GRAV = 9.8          # gravedad, m/s²
MASA = 68.1         # masa del paracaidista, kg
TIEMPO = 10.0       # tiempo de caída, s
VEL = 44.0          # velocidad medida, m/s
>>>>>>> Stashed changes

A, B = 0.5, 1.5   # intervalo de los métodos cerrados
X0 = 1.0         # inicio de los métodos abiertos
DELTA = 0.01      # incremento de la secante modificada
TOL = 0.5           # tolerancia: ea en %
NMAX = 50           # máximo de iteraciones


def f(x):
    """La función cuya raíz se busca."""
    return LD/LA*math.cos(x) - LD/LC*math.cos(TH2) + (LA*LA - LB*LB + LC*LC + LD*LD)/(2*LA*LC) - math.cos(TH2 - x)


def fp(x):
    """Su derivada, para Newton-Raphson."""
    return -LD/LA*math.sin(x) - math.sin(TH2 - x)


def g(x):
    """Despeje x = g(x) para punto fijo."""
    return x + f(x)/2

# ====================================================================


ENC_CERRADO = "   k             a             b             x            f(x)     ea (%)"
ENC_ABIERTO = "   k             x            f(x)     ea (%)"
ENC_RESUMEN = "            x  iter.     ea (%)            f(x)   método"


def error_aprox(nuevo, anterior):
    """Error relativo aproximado, en porcentaje: |(nuevo - anterior) / nuevo| · 100."""
    return abs((nuevo - anterior) / nuevo) * 100.0


def fila_cerrado(k, a, b, x, ea):
    texto = f"{ea:10.4f}" if ea is not None else f"{'-':>10}"
    print(f"{k:4d} {a:13.6f} {b:13.6f} {x:13.6f} {f(x):15.6e} {texto}")


def fila_abierto(k, x, ea):
    texto = f"{ea:10.4f}" if ea is not None else f"{'-':>10}"
    print(f"{k:4d} {x:13.6f} {f(x):15.6e} {texto}")


def cierre(r):
    if r["ok"]:
        print(f"   Raíz aproximada: {r['x']:.6f}  "
              f"({r['k']} iteraciones, ea = {r['ea']:.4f} %)")
    else:
        print(f"   No alcanzó la tolerancia en {NMAX} iteraciones.")
    print()


def biseccion(a, b):
    """Bisección: parte el intervalo a la mitad y conserva la mitad con cambio de signo."""
    r = {"nombre": "Bisección", "x": 0.0, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"1. Bisección en [{a:g}, {b:g}]")
    print(ENC_CERRADO)
    x_ant = 0.0
    for k in range(1, NMAX + 1):
        x = (a + b) / 2.0                        # punto medio
        ea = error_aprox(x, x_ant) if k > 1 else None
        fila_cerrado(k, a, b, x, ea)
        r.update(x=x, ea=ea or 0.0, k=k)
        r["historia"].append((k, x, ea))
        if k > 1 and ea <= TOL:
            r["ok"] = True
            break
        if f(a) * f(x) < 0.0:
            b = x                                # la raíz está en [a, x]
        else:
            a = x                                # la raíz está en [x, b]
        x_ant = x
    cierre(r)
    return r


def falsa_posicion(a, b):
    """Falsa posición: corta la recta que une (a, f(a)) y (b, f(b)) con el eje x."""
    r = {"nombre": "Falsa posición", "x": 0.0, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"2. Falsa posición en [{a:g}, {b:g}]")
    print(ENC_CERRADO)
    x_ant = 0.0
    for k in range(1, NMAX + 1):
        x = b - f(b) * (a - b) / (f(a) - f(b))   # cero de la recta
        ea = error_aprox(x, x_ant) if k > 1 else None
        fila_cerrado(k, a, b, x, ea)
        r.update(x=x, ea=ea or 0.0, k=k)
        r["historia"].append((k, x, ea))
        if k > 1 and ea <= TOL:
            r["ok"] = True
            break
        if f(a) * f(x) < 0.0:
            b = x
        else:
            a = x
        x_ant = x
    cierre(r)
    return r


def punto_fijo(x):
    """Punto fijo: repite x <- g(x)."""
    r = {"nombre": "Punto fijo", "x": x, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"3. Punto fijo desde x0 = {x:g}, con {DESCR_G}")
    print(ENC_ABIERTO)
    fila_abierto(0, x, None)
    for k in range(1, NMAX + 1):
        x_nuevo = g(x)
        ea = error_aprox(x_nuevo, x)
        x = x_nuevo
        fila_abierto(k, x, ea)
        r.update(x=x, ea=ea, k=k)
        r["historia"].append((k, x, ea))
        if ea <= TOL:
            r["ok"] = True
            break
    cierre(r)
    return r


def newton(x):
    """Newton-Raphson: el cero de la recta tangente en x."""
    r = {"nombre": "Newton-Raphson", "x": x, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"4. Newton-Raphson desde x0 = {x:g}")
    print(ENC_ABIERTO)
    fila_abierto(0, x, None)
    for k in range(1, NMAX + 1):
        x_nuevo = x - f(x) / fp(x)
        ea = error_aprox(x_nuevo, x)
        x = x_nuevo
        fila_abierto(k, x, ea)
        r.update(x=x, ea=ea, k=k)
        r["historia"].append((k, x, ea))
        if ea <= TOL:
            r["ok"] = True
            break
    cierre(r)
    return r


def secante_modificada(x, delta):
    """Secante modificada: Newton con la derivada aproximada por una diferencia."""
    r = {"nombre": "Secante modificada", "x": x, "ea": 0.0, "k": 0, "ok": False, "historia": []}
    print(f"5. Secante modificada desde x0 = {x:g}, delta = {delta:g}")
    print(ENC_ABIERTO)
    fila_abierto(0, x, None)
    for k in range(1, NMAX + 1):
        x_nuevo = x - delta * f(x) / (f(x + delta) - f(x))
        ea = error_aprox(x_nuevo, x)
        x = x_nuevo
        fila_abierto(k, x, ea)
        r.update(x=x, ea=ea, k=k)
        r["historia"].append((k, x, ea))
        if ea <= TOL:
            r["ok"] = True
            break
    cierre(r)
    return r


def graficar(resultados, carpeta="img"):
    """Guarda dos figuras en la carpeta img/:

    1. img/funcion.png: f(x) en [A, B], la recta y = 0 y la raíz de cada método.
    2. img/convergencia.png: ea (%) contra k, una curva por método, con el eje
       vertical en escala logarítmica y la tolerancia como línea horizontal.
    """
    os.makedirs(carpeta, exist_ok=True)
    # COMPLETAR: las dos figuras que se describen arriba.
    #
    # Cada elemento de `resultados` es un diccionario con:
    #   r["nombre"]    nombre del método
    #   r["x"]         raíz aproximada
    #   r["k"]         iteraciones realizadas
    #   r["historia"]  lista de tuplas (k, x_k, ea_k); en la primera fila de los
    #                  métodos cerrados ea_k vale None, y no se grafica.
    #
    # Funciones útiles: plt.figure, plt.plot, plt.semilogy, plt.axhline,
    # plt.xlabel, plt.ylabel, plt.title, plt.legend, plt.grid, plt.savefig y
    # plt.close. Guarde con plt.savefig(os.path.join(carpeta, "funcion.png")).
    print("graficar(): falta completar; todavía no se generan las figuras.")


def main():
    print("Práctica 2 · Raíces de ecuaciones no lineales · Python")
    print(DESCRIPCION)
    print(f"Tolerancia: ea <= {TOL:g} %, máximo {NMAX} iteraciones")
    print()
    resultados = [biseccion(A, B), falsa_posicion(A, B), punto_fijo(X0),
                  newton(X0), secante_modificada(X0, DELTA)]

    print("Resumen")
    print(ENC_RESUMEN)
    for r in resultados:
        aviso = "" if r["ok"] else " (no convergió)"
        print(f"{r['x']:13.6f} {r['k']:6d} {r['ea']:10.4f} {f(r['x']):15.6e}   {r['nombre']}{aviso}")
    print()

    # Verificación: SciPy encuentra la raíz con precisión de máquina.
    referencia = brentq(f, A, B, xtol=1e-14)
    print(f"Verificación con SciPy, brentq en [{A:g}, {B:g}]: x = {referencia:.9f}")
    print("   Error verdadero, en %:")
    for r in resultados:
        et = abs((referencia - r["x"]) / referencia) * 100.0
        print(f"   {et:10.6f}   {r['nombre']}")
    print()

    graficar(resultados)


if __name__ == "__main__":
    main()
