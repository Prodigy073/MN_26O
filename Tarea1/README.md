#### Tarea 1

## Métodos Numéricos (1151039), trimestre 26-O, licenciatura en ingeniería mecánica, Juan José Fernandez Gonzalez (2223036835).
#### 10 de octubre de 2026

#### Ejercicio 2

# ¿Qué son los métodos numéricos?
>Los métodos numéricos son herramientas muy poderosas para la solución de problemas. Son capaces de manipular sistemas de ecuaciones grandes, manejar no linealidades y resolver geometrías complicadas, comunes en la práctica de la ingeniería y, a menudo, imposibles de resolver en forma analítica. (Chapra, 2015).

Por lo tanto, la utilización de estos métodos permiten al usuario aventajarse y armarse para enfrentar situaciones en las que puede parecer imposible resolver un problema, encontrar un resultado o calcular una operación que, de hacerlo de forma manual o tradicional, se volvería muy tediosa. En general, aumentan la capacidad de un ingeniero para resolver problemas. A diferencia de un modelo matemático los métodos numéricos no resuelven un problema de manera general, si no que lo hacen para valores específicos, que pueden usarse posteriormente para estimar otros y así sucesivamente. 

Con esto como base, ahora se puede tocar el tema de las aproximaciones y de la función del error. 

>La esencia del análisis numérico no es buscar una respuesta perfecta, sino acotar y controlar el error para garantizar que la aproximación sea segura para la toma de decisiones. (Burden, 2011).

De acuerdo con Burden y Faires, hay un error de truncamiento el cual surge de reemplazar un procedimiento matemático por una aproximación finita. Y un error de redondeo, el cual ocurre debido a la limitada capacidad de las computadoras, pues tienen una cantidad finita de memoria. 

# ¿Cómo se aplican en ingeniería?
En mi caso estoy estudiando ingeniería mecánica, en la cual existen varias opciones donde se pueden aplicar métodos numéricos. A continuación se presentan dos ejemplos:

1. Transferencia de calor en piezas complejas.
Aquí se calcula el gradiente de temperatura en un componente de geometría compleja, como un bloque de motor o un disipador de aletas. El modelo matemático que    describe  el comportamiento del calor es la ecuación de Fourier, el cual solo tiene solución para formas ideales, como un cubo o un cilindro. Por lo que para     formas mas complejas su uso se ve limitado. Por ello se utiliza el "Método de elementos finitos" para dividir la geometría compleja y miles de pequeños           triángulos, permitiéndole al software resolver algebraicamente el flujo de calor atreves de las geometrías simplificadas. 

2. Dinámica de sistemas de suspensión no lineales (Vibraciones).
Aquí se calcula el desplazamiento, la velocidad y la aceleración del chasis de un automóvil a lo largo del tiempo después de que la llanta impacta contra un      bache. Si la suspensión estuviera hecha de un resorte ideal sin masa, la ecuación arrojaría una fórmula analítica perfecta de senos y cosenos (movimiento armónico simple). Sin embargo, un auto real utiliza amortiguadores hidráulicos cuya resistencia cambia según la velocidad del impacto, y resortes que se endurecen a medida que se comprimen. Esto genera una ecuación diferencial ordinaria no lineal. Las matemáticas no ofrecen una solución analítica para estas ecuaciones. Por lo tanto, se aplican métodos numéricos como Runge-Kutta para calcular las fuerzas y la posición del vehículo en minúsculos intervalos de tiempo a lo largo del impacto, recreando el comportamiento físico real.

# ¿Qué herramientas se usan para trabajar con métodos numéricos?
Las herramientas de programación y software que se utilizan son: 

- Microsoft Excel (junto con macros en VBA / Visual Basic for Applications).
- MATLAB (utilizando scripts y archivos M, o M-files).
- Mathcad (como herramienta de cálculo y documentación matemática).

# ¿Qué herramientas usamos en este curso?
Docker, para la creación de contenedores en una maquina virtual. Donde se alojaran los diferentes archivos de trabajo del curso y nos permitirán un manejo eficaz de estos a través del uso de  consola y de los siguientes comandos: comandos up -d, exec, stop, down, ps y logs.

GNU Octave, es una alternativa gratuita al software Matlab, los cuales son un herramienta para el calculo numérico y el tratamiento de datos.

Python y C, son leguajes de programación que nos permiten la implantación de código y la ejecución de los mismos, para llevar acabó los métodos numéricos y que los entienda la computadora, para que posteriormente se usen estos métodos en la resolución de ejercicios o problemas propuestos por el profesor.  

# Bibliografia
[1] Chapra, S. C., & Canale, R. P. (2015). Métodos Numéricos para Ingenieros (7a ed.). McGraw-Hill.
[2] Chapra, S. C., & Canale, R. P. (2015). Métodos Numéricos para Ingenieros (7a ed.). McGraw-Hill.






