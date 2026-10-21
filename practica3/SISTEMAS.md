# Sistemas de ingeniería de la Práctica 3

Datos didácticos sintéticos para practicar; no son mediciones de instalaciones reales. El profesor asigna un caso por equipo, de una licenciatura de sus integrantes. Se cambia sólo el archivo de datos, no el algoritmo.

## caso01 · Ambiental · variante 1

Concentraciones en una cadena de reactores con intercambio y remoción.

Incógnitas: x₁ a x3 en mg/L. A en L/h; b en mg/h.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     5.00000   -2.00000    0.00000
    -2.00000    7.00000   -2.00000
     0.00000   -2.00000    5.00000
b = 5.50000 11.00000 16.50000
```

Archivo: `casos/caso01.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso02 · Ambiental · variante 2

Concentraciones en una cadena de reactores con intercambio y remoción.

Incógnitas: x₁ a x4 en mg/L. A en L/h; b en mg/h.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     5.30000   -2.30000    0.00000    0.00000
    -2.30000    7.60000   -2.30000    0.00000
     0.00000   -2.30000    7.60000   -2.30000
     0.00000    0.00000   -2.30000    5.30000
b = 6.00000 12.00000 18.00000 24.00000
```

Archivo: `casos/caso02.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso03 · Ambiental · variante 3

Concentraciones en una cadena de reactores con intercambio y remoción.

Incógnitas: x₁ a x5 en mg/L. A en L/h; b en mg/h.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     5.60000   -2.60000    0.00000    0.00000    0.00000
    -2.60000    8.20000   -2.60000    0.00000    0.00000
     0.00000   -2.60000    8.20000   -2.60000    0.00000
     0.00000    0.00000   -2.60000    8.20000   -2.60000
     0.00000    0.00000    0.00000   -2.60000    5.60000
b = 6.50000 13.00000 19.50000 26.00000 32.50000
```

Archivo: `casos/caso03.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

## caso04 · Civil · variante 1

Desplazamientos de pisos unidos por resortes y apoyos laterales.

Incógnitas: x₁ a x3 en mm. A en kN/mm; b en kN.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
    10.00000   -4.00000    0.00000
    -4.00000   14.00000   -4.00000
     0.00000   -4.00000   10.00000
b = 11.00000 22.00000 33.00000
```

Archivo: `casos/caso04.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso05 · Civil · variante 2

Desplazamientos de pisos unidos por resortes y apoyos laterales.

Incógnitas: x₁ a x4 en mm. A en kN/mm; b en kN.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
    10.60000   -4.60000    0.00000    0.00000
    -4.60000   15.20000   -4.60000    0.00000
     0.00000   -4.60000   15.20000   -4.60000
     0.00000    0.00000   -4.60000   10.60000
b = 12.00000 24.00000 36.00000 48.00000
```

Archivo: `casos/caso05.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso06 · Civil · variante 3

Desplazamientos de pisos unidos por resortes y apoyos laterales.

Incógnitas: x₁ a x5 en mm. A en kN/mm; b en kN.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
    11.20000   -5.20000    0.00000    0.00000    0.00000
    -5.20000   16.40000   -5.20000    0.00000    0.00000
     0.00000   -5.20000   16.40000   -5.20000    0.00000
     0.00000    0.00000   -5.20000   16.40000   -5.20000
     0.00000    0.00000    0.00000   -5.20000   11.20000
b = 13.00000 26.00000 39.00000 52.00000 65.00000
```

Archivo: `casos/caso06.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

## caso07 · Computación · variante 1

Valores suavizados de una señal en un grafo de vecinos.

Incógnitas: x₁ a x3 en unidad de señal. A en adimensional; b en unidad de señal.

Cada nodo penaliza su diferencia con los vecinos y su alejamiento de un dato de entrada. El vector b reúne el peso de fidelidad multiplicado por los datos observados.

```text
A =
     3.00000   -1.00000    0.00000
    -1.00000    4.00000   -1.00000
     0.00000   -1.00000    3.00000
b = 3.30000 6.60000 9.90000
```

Archivo: `casos/caso07.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso08 · Computación · variante 2

Valores suavizados de una señal en un grafo de vecinos.

Incógnitas: x₁ a x4 en unidad de señal. A en adimensional; b en unidad de señal.

Cada nodo penaliza su diferencia con los vecinos y su alejamiento de un dato de entrada. El vector b reúne el peso de fidelidad multiplicado por los datos observados.

```text
A =
     3.15000   -1.15000    0.00000    0.00000
    -1.15000    4.30000   -1.15000    0.00000
     0.00000   -1.15000    4.30000   -1.15000
     0.00000    0.00000   -1.15000    3.15000
b = 3.60000 7.20000 10.80000 14.40000
```

Archivo: `casos/caso08.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso09 · Computación · variante 3

Valores suavizados de una señal en un grafo de vecinos.

Incógnitas: x₁ a x5 en unidad de señal. A en adimensional; b en unidad de señal.

Cada nodo penaliza su diferencia con los vecinos y su alejamiento de un dato de entrada. El vector b reúne el peso de fidelidad multiplicado por los datos observados.

```text
A =
     3.30000   -1.30000    0.00000    0.00000    0.00000
    -1.30000    4.60000   -1.30000    0.00000    0.00000
     0.00000   -1.30000    4.60000   -1.30000    0.00000
     0.00000    0.00000   -1.30000    4.60000   -1.30000
     0.00000    0.00000    0.00000   -1.30000    3.30000
b = 3.90000 7.80000 11.70000 15.60000 19.50000
```

Archivo: `casos/caso09.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

## caso10 · Eléctrica · variante 1

Voltajes en nodos con conductancias entre vecinos y a tierra.

Incógnitas: x₁ a x3 en V. A en mS; b en mA.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     6.00000   -2.00000    0.00000
    -2.00000    8.00000   -2.00000
     0.00000   -2.00000    6.00000
b = 6.60000 13.20000 19.80000
```

Archivo: `casos/caso10.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso11 · Eléctrica · variante 2

Voltajes en nodos con conductancias entre vecinos y a tierra.

Incógnitas: x₁ a x4 en V. A en mS; b en mA.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     6.30000   -2.30000    0.00000    0.00000
    -2.30000    8.60000   -2.30000    0.00000
     0.00000   -2.30000    8.60000   -2.30000
     0.00000    0.00000   -2.30000    6.30000
b = 7.20000 14.40000 21.60000 28.80000
```

Archivo: `casos/caso11.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso12 · Eléctrica · variante 3

Voltajes en nodos con conductancias entre vecinos y a tierra.

Incógnitas: x₁ a x5 en V. A en mS; b en mA.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     6.60000   -2.60000    0.00000    0.00000    0.00000
    -2.60000    9.20000   -2.60000    0.00000    0.00000
     0.00000   -2.60000    9.20000   -2.60000    0.00000
     0.00000    0.00000   -2.60000    9.20000   -2.60000
     0.00000    0.00000    0.00000   -2.60000    6.60000
b = 7.80000 15.60000 23.40000 31.20000 39.00000
```

Archivo: `casos/caso12.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

## caso13 · Electrónica · variante 1

Voltajes de polarización en una red resistiva de etapas.

Incógnitas: x₁ a x3 en V. A en mS; b en mA.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     2.00000   -0.50000    0.00000
    -0.50000    2.50000   -0.50000
     0.00000   -0.50000    2.00000
b = 2.20000 4.40000 6.60000
```

Archivo: `casos/caso13.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso14 · Electrónica · variante 2

Voltajes de polarización en una red resistiva de etapas.

Incógnitas: x₁ a x4 en V. A en mS; b en mA.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     2.07500   -0.57500    0.00000    0.00000
    -0.57500    2.65000   -0.57500    0.00000
     0.00000   -0.57500    2.65000   -0.57500
     0.00000    0.00000   -0.57500    2.07500
b = 2.40000 4.80000 7.20000 9.60000
```

Archivo: `casos/caso14.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso15 · Electrónica · variante 3

Voltajes de polarización en una red resistiva de etapas.

Incógnitas: x₁ a x5 en V. A en mS; b en mA.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     2.15000   -0.65000    0.00000    0.00000    0.00000
    -0.65000    2.80000   -0.65000    0.00000    0.00000
     0.00000   -0.65000    2.80000   -0.65000    0.00000
     0.00000    0.00000   -0.65000    2.80000   -0.65000
     0.00000    0.00000    0.00000   -0.65000    2.15000
b = 2.60000 5.20000 7.80000 10.40000 13.00000
```

Archivo: `casos/caso15.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

## caso16 · Física · variante 1

Incrementos de temperatura en segmentos de una barra con pérdidas al ambiente.

Incógnitas: x₁ a x3 en K. A en W/K; b en W.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     5.00000   -2.00000    0.00000
    -2.00000    7.00000   -2.00000
     0.00000   -2.00000    5.00000
b = 5.50000 11.00000 16.50000
```

Archivo: `casos/caso16.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso17 · Física · variante 2

Incrementos de temperatura en segmentos de una barra con pérdidas al ambiente.

Incógnitas: x₁ a x4 en K. A en W/K; b en W.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     5.30000   -2.30000    0.00000    0.00000
    -2.30000    7.60000   -2.30000    0.00000
     0.00000   -2.30000    7.60000   -2.30000
     0.00000    0.00000   -2.30000    5.30000
b = 6.00000 12.00000 18.00000 24.00000
```

Archivo: `casos/caso17.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso18 · Física · variante 3

Incrementos de temperatura en segmentos de una barra con pérdidas al ambiente.

Incógnitas: x₁ a x5 en K. A en W/K; b en W.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     5.60000   -2.60000    0.00000    0.00000    0.00000
    -2.60000    8.20000   -2.60000    0.00000    0.00000
     0.00000   -2.60000    8.20000   -2.60000    0.00000
     0.00000    0.00000   -2.60000    8.20000   -2.60000
     0.00000    0.00000    0.00000   -2.60000    5.60000
b = 6.50000 13.00000 19.50000 26.00000 32.50000
```

Archivo: `casos/caso18.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

## caso19 · Industrial · variante 1

Niveles de producción con consumo de insumos entre etapas.

Incógnitas: x₁ a x3 en lote/h. A en adimensional; b en lote/h.

Cada ecuación expresa producción de una etapa menos el consumo acoplado de las etapas vecinas, igual a su demanda neta. Los coeficientes son adimensionales.

```text
A =
     1.90000   -0.40000    0.00000
    -0.40000    1.90000   -0.40000
     0.00000   -0.40000    1.90000
b = 2.42000 4.84000 7.26000
```

Archivo: `casos/caso19.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso20 · Industrial · variante 2

Niveles de producción con consumo de insumos entre etapas.

Incógnitas: x₁ a x4 en lote/h. A en adimensional; b en lote/h.

Cada ecuación expresa producción de una etapa menos el consumo acoplado de las etapas vecinas, igual a su demanda neta. Los coeficientes son adimensionales.

```text
A =
     2.00000   -0.46000    0.00000    0.00000
    -0.46000    2.00000   -0.46000    0.00000
     0.00000   -0.46000    2.00000   -0.46000
     0.00000    0.00000   -0.46000    2.00000
b = 2.64000 5.28000 7.92000 10.56000
```

Archivo: `casos/caso20.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso21 · Industrial · variante 3

Niveles de producción con consumo de insumos entre etapas.

Incógnitas: x₁ a x5 en lote/h. A en adimensional; b en lote/h.

Cada ecuación expresa producción de una etapa menos el consumo acoplado de las etapas vecinas, igual a su demanda neta. Los coeficientes son adimensionales.

```text
A =
     2.10000   -0.52000    0.00000    0.00000    0.00000
    -0.52000    2.10000   -0.52000    0.00000    0.00000
     0.00000   -0.52000    2.10000   -0.52000    0.00000
     0.00000    0.00000   -0.52000    2.10000   -0.52000
     0.00000    0.00000    0.00000   -0.52000    2.10000
b = 2.86000 5.72000 8.58000 11.44000 14.30000
```

Archivo: `casos/caso21.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

## caso22 · Mecánica · variante 1

Desplazamientos de masas acopladas por resortes.

Incógnitas: x₁ a x3 en mm. A en N/mm; b en N.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     8.00000   -3.00000    0.00000
    -3.00000   11.00000   -3.00000
     0.00000   -3.00000    8.00000
b = 8.80000 17.60000 26.40000
```

Archivo: `casos/caso22.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso23 · Mecánica · variante 2

Desplazamientos de masas acopladas por resortes.

Incógnitas: x₁ a x4 en mm. A en N/mm; b en N.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     8.45000   -3.45000    0.00000    0.00000
    -3.45000   11.90000   -3.45000    0.00000
     0.00000   -3.45000   11.90000   -3.45000
     0.00000    0.00000   -3.45000    8.45000
b = 9.60000 19.20000 28.80000 38.40000
```

Archivo: `casos/caso23.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso24 · Mecánica · variante 3

Desplazamientos de masas acopladas por resortes.

Incógnitas: x₁ a x5 en mm. A en N/mm; b en N.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     8.90000   -3.90000    0.00000    0.00000    0.00000
    -3.90000   12.80000   -3.90000    0.00000    0.00000
     0.00000   -3.90000   12.80000   -3.90000    0.00000
     0.00000    0.00000   -3.90000   12.80000   -3.90000
     0.00000    0.00000    0.00000   -3.90000    8.90000
b = 10.40000 20.80000 31.20000 41.60000 52.00000
```

Archivo: `casos/caso24.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

## caso25 · Metalúrgica · variante 1

Incrementos de temperatura en zonas de un horno con intercambio térmico.

Incógnitas: x₁ a x3 en K. A en W/K; b en W.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     4.00000   -1.50000    0.00000
    -1.50000    5.50000   -1.50000
     0.00000   -1.50000    4.00000
b = 4.40000 8.80000 13.20000
```

Archivo: `casos/caso25.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso26 · Metalúrgica · variante 2

Incrementos de temperatura en zonas de un horno con intercambio térmico.

Incógnitas: x₁ a x4 en K. A en W/K; b en W.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     4.22500   -1.72500    0.00000    0.00000
    -1.72500    5.95000   -1.72500    0.00000
     0.00000   -1.72500    5.95000   -1.72500
     0.00000    0.00000   -1.72500    4.22500
b = 4.80000 9.60000 14.40000 19.20000
```

Archivo: `casos/caso26.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso27 · Metalúrgica · variante 3

Incrementos de temperatura en zonas de un horno con intercambio térmico.

Incógnitas: x₁ a x5 en K. A en W/K; b en W.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     4.45000   -1.95000    0.00000    0.00000    0.00000
    -1.95000    6.40000   -1.95000    0.00000    0.00000
     0.00000   -1.95000    6.40000   -1.95000    0.00000
     0.00000    0.00000   -1.95000    6.40000   -1.95000
     0.00000    0.00000    0.00000   -1.95000    4.45000
b = 5.20000 10.40000 15.60000 20.80000 26.00000
```

Archivo: `casos/caso27.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

## caso28 · Química · variante 1

Concentraciones en una cadena de mezcladores con recirculación.

Incógnitas: x₁ a x3 en mol/L. A en L/h; b en mol/h.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     3.50000   -1.00000    0.00000
    -1.00000    4.50000   -1.00000
     0.00000   -1.00000    3.50000
b = 3.85000 7.70000 11.55000
```

Archivo: `casos/caso28.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 3 incógnitas.

## caso29 · Química · variante 2

Concentraciones en una cadena de mezcladores con recirculación.

Incógnitas: x₁ a x4 en mol/L. A en L/h; b en mol/h.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     3.65000   -1.15000    0.00000    0.00000
    -1.15000    4.80000   -1.15000    0.00000
     0.00000   -1.15000    4.80000   -1.15000
     0.00000    0.00000   -1.15000    3.65000
b = 4.20000 8.40000 12.60000 16.80000
```

Archivo: `casos/caso29.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 4 incógnitas.

## caso30 · Química · variante 3

Concentraciones en una cadena de mezcladores con recirculación.

Incógnitas: x₁ a x5 en mol/L. A en L/h; b en mol/h.

Balance local: el coeficiente diagonal reúne el intercambio con vecinos y el apoyo, remoción o pérdida local; los coeficientes negativos enlazan nodos vecinos. b contiene las fuentes o cargas impuestas.

```text
A =
     3.80000   -1.30000    0.00000    0.00000    0.00000
    -1.30000    5.10000   -1.30000    0.00000    0.00000
     0.00000   -1.30000    5.10000   -1.30000    0.00000
     0.00000    0.00000   -1.30000    5.10000   -1.30000
     0.00000    0.00000    0.00000   -1.30000    3.80000
b = 4.55000 9.10000 13.65000 18.20000 22.75000
```

Archivo: `casos/caso30.dat`. Dibujen la cadena de nodos y expliquen qué significa la ecuación de un nodo interior. Cada variante tiene 5 incógnitas.

