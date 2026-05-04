import math

# ──────────────────────────────────────────────
#  Método de Falsa Posición (Regula Falsi)
# ──────────────────────────────────────────────

def regula_falsi():
    print("=" * 55)
    print("      MÉTODO DE FALSA POSICIÓN (Regula Falsi)")
    print("=" * 55)

    # ── Ingresar f(x) ──────────────────────────────────────
    print("\nEscribe la función f(x) usando sintaxis Python.")
    print("Funciones disponibles: sin, cos, tan, exp, log, sqrt, pi, e")
    print("Ejemplo: x**3 - x - 2   o   math.exp(x) - 3*x\n")

    func_str = input("f(x) = ")

    def f(x):
        return eval(func_str, {"x": x, "math": math,
                               "sin": math.sin, "cos": math.cos,
                               "tan": math.tan, "exp": math.exp,
                               "log": math.log, "sqrt": math.sqrt,
                               "pi": math.pi, "e": math.e})

    # ── Ingresar intervalo [a, b] ───────────────────────────
    print()
    while True:
        try:
            a = float(input("Ingresa el extremo izquierdo  a: "))
            b = float(input("Ingresa el extremo derecho    b: "))
            if f(a) * f(b) < 0:
                break
            else:
                print("  ⚠  f(a)·f(b) debe ser < 0. El intervalo no contiene una raíz (o contiene un número par). Intenta de nuevo.\n")
        except Exception as err:
            print(f"  ⚠  Error al evaluar la función: {err}. Intenta de nuevo.\n")

    # ── Tolerancia ε ───────────────────────────────────────
    eps = float(input("Ingresa la tolerancia ε (ej. 0.0001): "))

    # ── Número máximo de iteraciones ───────────────────────
    max_iter = int(input("Ingresa el número máximo de iteraciones: "))

    # ── Tabla de encabezado ────────────────────────────────
    print()
    print("-" * 75)
    print(f"{'Iter':>4}  {'a':>12}  {'b':>12}  {'c':>14}  {'f(c)':>14}  {'|f(c)|':>10}")
    print("-" * 75)

    convergio = False
    iter_count = 0

    for i in range(1, max_iter + 1):
        iter_count = i
        fa = f(a)
        fb = f(b)

        # Fórmula de falsa posición
        c = a - fa * (b - a) / (fb - fa)
        fc = f(c)

        print(f"{i:>4}  {a:>12.6f}  {b:>12.6f}  {c:>14.8f}  {fc:>14.8f}  {abs(fc):>10.2e}")

        # Criterio de convergencia
        if abs(fc) < eps:
            convergio = True
            break

        # Actualizar intervalo
        if fa * fc < 0:
            b = c
        else:
            a = c

    print("-" * 75)
    print()

    # ── Resultado ──────────────────────────────────────────
    if convergio:
        print(f"✅  ¡Convergió en la iteración {iter_count}!")
        print(f"    Raíz aproximada: c = {c:.10f}")
        print(f"    |f(c)| = {abs(fc):.2e}  <  ε = {eps}")
    else:
        print(f"⚠   Se alcanzó el máximo de {max_iter} iteraciones sin converger.")
        print(f"    Mejor aproximación: c = {c:.10f}")
        print(f"    |f(c)| = {abs(fc):.2e}  (ε = {eps})")

    print()


if __name__ == "__main__":
    regula_falsi()