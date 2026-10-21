# Cómo correr la Práctica 3

## Repositorio del equipo

Sigan en el mismo repositorio. Copien sólo `practica3/` de ContenedorPractica3 a la raíz del repositorio. Conserven el Dockerfile y compose.yaml del curso. Agreguen `practica3/sistemas` al .gitignore para ignorar el ejecutable. Los CSV de `salidas/` y las gráficas de `resultados/` forman parte de la entrega y sí deben versionarse.

```bash
git switch main
git pull
git switch -c practica3
docker compose up -d
docker compose exec metodos bash
cd practica3
mkdir -p salidas img
octave sistemas.m casos/ejemplo.dat > salidas/ejemplo_octave.csv
python3 sistemas.py casos/ejemplo.dat > salidas/ejemplo_python.csv
gcc -O2 -std=c17 -Wall -Wextra -o sistemas sistemas.c -lm
./sistemas casos/ejemplo.dat > salidas/ejemplo_c.csv
```

Al copiar el entorno completo en una carpeta aparte, usar `docker compose up -d --build` la primera vez. El servicio se llama metodos. La imagen compartida del curso es metodos-1151039:26o.

## Completar C

COMPLETAR 1: escoger el mayor pivote en valor absoluto con el vector p.
COMPLETAR 2: actualizar un coeficiente al eliminar.
COMPLETAR 3: despejar una incógnita por sustitución hacia atrás.
COMPLETAR 4: actualización de Jacobi con todos los valores anteriores.
COMPLETAR 5: actualización de Gauss-Seidel con lo recién calculado.
COMPLETAR 6: combinación relajada de SOR.
COMPLETAR 7: error relativo del vector con norma euclidiana, en porcentaje.

Mientras falten, C compila pero no produce la referencia. Puede terminar con MAX_ITER: es una señal de revisión, no un éxito. El paro exige DOS condiciones: ea₂ ≤ 0.5 % y ‖b−Ax‖∞/‖b‖∞ ≤ 1e-6. Máximo: 200 vueltas. Inicio: vector cero.

Las salidas de C, Python y Octave deben coincidir a la precisión impresa; se admite una diferencia de redondeo final. Comparar estados e iteraciones y, numéricamente, atol=1e-8 y rtol=1e-7. No comparar la fila LU-2b contra la solución de b: resuelve la segunda carga.

## Caso del equipo y gráficas

Sustituir caso01 por el asignado. No editar los algoritmos para cambiar el problema.

```bash
./sistemas casos/caso01.dat > salidas/caso01_c.csv
octave sistemas.m casos/caso01.dat > salidas/caso01_octave.csv
python3 sistemas.py casos/caso01.dat > salidas/caso01_python.csv
python3 sistemas.py casos/caso01.dat 1.1 --analisis
```

Completen graficar() en sistemas.py. Recibe un diccionario info con `iterativos` (filas con k, ea, res), y `barrido` (lam, k, estado, res). Guardar convergencia.png con residuo relativo en escala logarítmica y relajacion.png con vueltas contra λ. Marcar aparte los que no convergen, sin presentarlos como una solución válida.

## Casos que enseñan a detectar problemas

```bash
./sistemas casos/pivote_cero.dat
./sistemas casos/pivote_pequeno.dat
python3 sistemas.py casos/spd.dat --analisis
python3 sistemas.py casos/mal_condicionado.dat --analisis
python3 sistemas.py casos/sin_solucion.dat --analisis
python3 sistemas.py casos/infinitas.dat --analisis
```

Los dos últimos muestran rangos y clasificación. LU no resuelve todos los sistemas singulares. Un fallo del algoritmo sin pivote puede ocurrir aunque sí exista solución única.

## Conflicto de Git entre dos integrantes

Desde practica3, los dos parten del MISMO commit. Cada uno crea su rama local (p3-integrante-a y p3-integrante-b), cambia la misma línea de COLABORACION.md y hace commit. Comparten las ramas con push. El responsable integra primero la rama a en practica3 y después la b. La segunda integración produce el conflicto. Leer ambos aportes, editar el archivo conservando ambos nombres, quitar los marcadores <<<<<<<, ======= y >>>>>>>, hacer git add y git commit. Registrar los commits y una captura. No generar el conflicto en los algoritmos numéricos.

Al terminar, abrir el Pull Request de practica3 a main, revisarlo e integrarlo. La entrega es la liga del repositorio y su historial.

## Captura de cada integrante

```bash
git switch practica3
git pull
docker compose up -d
docker compose exec metodos bash
cd practica3
gcc -O2 -std=c17 -Wall -Wextra -o sistemas sistemas.c -lm
./sistemas casos/caso01.dat
exit
git add practica3/img/07-integrante-apellido.png practica3/README.md
git commit -m "Captura de Nombre Apellido en su computadora"
git push
```

En Windows, Win + Shift + S captura la terminal. Guarda la imagen en practica3/img/ con el nombre indicado.

## Si algo falla

`gcc` u `octave` no encontrados: entra al contenedor. CSV antiguo después de editar C: recompila. DIAGONAL_CERO: el iterativo no puede despejar ese orden. PIVOTE_NULO: revisa el pivoteo y la singularidad. NO_APLICA de Cholesky: comprueba simetría y definición positiva. MAX_ITER o DIVERGE: no afirmes que convergió. A menudo hay que ordenar las ecuaciones o elegir otro método.
