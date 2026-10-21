# Práctica 3 · Sistemas de ecuaciones lineales

UEA 1151039 · 26-O · UAM Azcapotzalco

| Dato | Información |
|---|---|
| Equipo y repositorio | |
| Integrantes y matrículas | |
| Caso asignado y licenciatura | |
| Variables y unidades | |

## 1. Ejemplo del curso

Capturas de Octave, Python, compilación y ejecución de C. Adjuntar CSV de los tres lenguajes en `salidas/`.

![Octave](img/01-octave.png)
![Python](img/02-python.png)
![Compilación](img/03-c-compilacion.png)
![C](img/04-c-ejecucion.png)

## 2. Las siete líneas de C

Indicar cada línea COMPLETAR y explicar qué calcula. No basta pegar el programa completo.

## 3. Nuestro sistema

Escribir A, b, unidades y significado de un renglón. Conservar el .dat original.

| Método | Vector x | Iteraciones | ea₂ (%) | Residuo relativo ∞ | Estado |
|---|---|---|---|---|---|
| Gauss sin pivote | | No aplica | No aplica | | |
| Gauss con pivote | | No aplica | No aplica | | |
| LU con 2b | | No aplica | No aplica | Se mide respecto de 2b | |
| Cholesky | | No aplica | No aplica | | |
| Jacobi | | | | | |
| Gauss-Seidel | | | | | |
| SOR, λ = 1.1 | | | | | |

Pegar las tablas completas de iteración o adjuntar los CSV. Python calcula cond∞(A), el error verdadero respecto de NumPy y los radios espectrales. Reportarlos y explicar las diferencias.

![Caso en C](img/05-c-caso.png)
![Caso en Python](img/06-python-caso.png)

## 4. Gráficas y relajación

Insertar `resultados/casoNN/img/convergencia.png` y `relajacion.png`. Sustituir casoNN por el asignado.
Reportar el λ que ganó dentro del barrido probado, cuántas vueltas necesitó y por qué no puede presentarse como óptimo universal.

## 5. Experimentos de diagnóstico

| Archivo o experimento | Qué observamos | Explicación |
|---|---|---|
| pivote_cero.dat | | |
| pivote_pequeno.dat | | |
| spd.dat y LU con 2b | | |
| mal_condicionado.dat y perturbación de b | | |
| sin_solucion.dat e infinitas.dat | | |
| Intercambio de filas 1 y 3 del ejemplo | | |

Cambiar sólo los renglones de A y las mismas componentes de b. Guardar el nuevo archivo como `casos/reordenado.dat`. No cambiar las columnas: las variables conservan su orden.

## 6. Conflicto de Git

Registrar los dos participantes, el archivo COLABORACION.md, los commits y una captura del conflicto resuelto. Enlazar el Pull Request de practica3 a main.

## 7. Evidencia de cada integrante

| Integrante | Usuario GitHub | Captura y commit |
|---|---|---|
| | | img/07-integrante-apellido.png |

Cada integrante ejecuta el C del caso del equipo en su computadora y agrega su captura con un commit propio.

## Análisis final

¿Qué método convino? ¿Qué cambió al reordenar las ecuaciones? ¿Un cambio pequeño del vector garantiza una solución correcta? ¿Qué indica cond∞(A)? ¿Por qué Cholesky no aplica al ejemplo no simétrico?

## Uso de inteligencia artificial y referencias

Herramienta utilizada y para qué, o ninguno. Citar fuentes consultadas.
