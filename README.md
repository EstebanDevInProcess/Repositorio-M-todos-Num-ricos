# Repositorio-M-todos-Num-ricos
los mejores codigos del pedazo
# Métodos Numéricos en Python

Programas de consola en Python que implementan siete métodos numéricos vistos en la asignatura de **Análisis Numérico** de la Universidad de Cundinamarca. Cada programa le pide al usuario la función y los parámetros, y muestra una tabla con cada iteración y su error.

El código se desarrolló con apoyo de herramientas de Inteligencia Artificial (*vibe coding*).

## Métodos incluidos

### Raíces de ecuaciones de una variable

| Método | Archivo | Datos que pide |
|---|---|---|
| Bisección | `Biseccion_Terminado.py` | f(x), intervalo [a, b], tolerancia, iteraciones |
| Falsa Posición (Regula Falsi) | `falsa_posicion.py` | f(x), intervalo [a, b], tolerancia, iteraciones |
| Secante | `secante.py` | f(x), dos valores iniciales x0 y x1, tolerancia, iteraciones |
| Newton-Raphson | `newthon.py` | f(x), valor inicial x0, tolerancia, iteraciones |
| Punto Fijo | `Metodo_de_punto_fijo.py` | g(x) tal que x = g(x), valor inicial x0, iteraciones, tolerancia |

### Sistemas de ecuaciones no lineales

| Método | Archivo | Datos que pide |
|---|---|---|
| Jacobi | `jacobi.py` | número de variables, despeje de cada variable, valores iniciales, tolerancia, iteraciones |
| Gauss-Seidel | `gauss.py` | número de variables, despeje de cada variable, valores iniciales, tolerancia, iteraciones |

En Jacobi, cada variable se calcula con los valores de la iteración anterior. En Gauss-Seidel, cada variable usa de inmediato los valores que ya se actualizaron en la misma iteración.

## Requisitos

- Python 3
- No necesita librerías externas (solo usa el módulo `math` de la librería estándar)

## Cómo ejecutarlos

Clona el repositorio y ejecuta el método que quieras:

```bash
git clone https://github.com/EstebanDevInProcess/Repositorio-M-todos-Num-ricos.git
cd Repositorio-M-todos-Num-ricos
python Biseccion_Terminado.py
```

Cada programa pide los datos uno por uno en la terminal.

## Cómo escribir las funciones

Las funciones se escriben con sintaxis de Python:

- Potencias: `x**3` (no `x^3`)
- Multiplicación explícita: `3*x` (no `3x`)
- Funciones matemáticas: `math.sin(x)`, `math.cos(x)`, `math.exp(x)`, `math.log(x)`, `math.sqrt(x)`

Notas por programa:

- **Newton-Raphson** solo acepta las funciones con el prefijo `math.` (por ejemplo, `math.sin(x)`).
- **Punto Fijo** solo acepta las funciones sin el prefijo (por ejemplo, `sin(x)`, `sqrt(x + 2)`).
- **Jacobi y Gauss-Seidel** usan las variables `x1`, `x2`, ..., `xn`.

## Ejemplos

**Bisección** con f(x) = `x**3 - x - 2` en [1, 2], tolerancia 0.0001 y 50 iteraciones:

```
  ✔ Convergió en la iteración 14 (no tenía caso seguir).

  Raíz aproximada  : c    = 1.52142334
```

**Punto Fijo** con g(x) = `cos(x)` y x0 = 1: converge a x ≈ 0.7390851.

**Gauss-Seidel** con el sistema

```
x² + y − 4 = 0
x + y² − 3 = 0
```

se despeja cada variable y se ingresa así:

```
x1 = sqrt(4 - x2)
x2 = sqrt(3 - x1)
```

Con valores iniciales x1 = 1 y x2 = 1, converge a x1 ≈ 1.68978, x2 ≈ 1.14465.

## Qué controla cada programa

- **Criterio de parada:** cada método se detiene cuando el error es menor que la tolerancia o cuando se alcanza el número máximo de iteraciones.
- **Validación de entradas:** Bisección y Falsa Posición verifican que f(a)·f(b) < 0. La Secante verifica que x0 ≠ x1. La mayoría de programas vuelve a pedir el dato si no es un número válido.
- **Casos de falla:**
  - Secante y Newton-Raphson se detienen si hay división por cero.
  - Newton-Raphson aproxima la derivada por diferencias centrales, así que no hace falta escribirla.
  - Punto Fijo avisa si los valores divergen.
  - Jacobi y Gauss-Seidel avisan si un valor sale del dominio de la función (por ejemplo, la raíz de un número negativo).

## Autor

Juan Esteban Castillo Olaya, estudiante de Ingeniería de Sistemas y Computación, Universidad de Cundinamarca.
