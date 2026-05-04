import math

def biseccion():
    print("=" * 55)
    print("      MÉTODO DE BISECCIÓN - Búsqueda de Raíces")
    print("=" * 55)

    # ── Función ──────────────────────────────────────────────
    print("\nEscribe la función usando sintaxis Python:")
    print("  Potencias  : x**3  (no uses x³ ni x^3)")
    print("  Seno/coseno: math.sin(x), math.cos(x)")
    print("  Exponencial: math.exp(x)")
    print("  Logaritmo  : math.log(x)")
    print("\nEjemplos:  x**3 - x - 2   |   math.sin(x) - 0.5   |   x**2 - 4")

    while True:
        expr = input("\nIngresa la función f(x): ").strip()
        try:
            def f(x):
                return eval(expr, {"x": x, "math": math, **vars(math)})
            f(1.0)
            break
        except Exception as e:
            print(f"  Error en la función: {e}. Intenta de nuevo.")

    # ── Intervalo [a, b] ─────────────────────────────────────
    print("\nIngresa el intervalo [a, b] donde f(a)·f(b) < 0")
    while True:
        try:
            a = float(input("  a = "))
            b = float(input("  b = "))
            fa, fb = f(a), f(b)
            if fa * fb < 0:
                break
            print(f"  f({a}) = {fa:.4f}  y  f({b}) = {fb:.4f}")
            print("  f(a)*f(b) debe ser negativo. Elige otro intervalo.")
        except Exception as e:
            print(f"  Error: {e}")

    # ── Tolerancia ───────────────────────────────────────────
    while True:
        try:
            tol = float(input("\nTolerancia ε (ej. 0.0001): "))
            if tol > 0:
                break
            print("  Debe ser un número positivo.")
        except ValueError:
            print("  Ingresa un número válido.")

    # ── Número máximo de iteraciones ─────────────────────────
    while True:
        try:
            n = int(input("¿Cuántas iteraciones deseas realizar? "))
            if n > 0:
                break
            print("  Debe ser un entero positivo.")
        except ValueError:
            print("  Ingresa un número entero válido.")

    # ── Tabla ────────────────────────────────────────────────
    print("\n" + "=" * 78)
    print(f"{'Iter':>4} | {'a':>12} | {'b':>12} | {'c=(a+b)/2':>12} | {'f(c)':>14} | {'|b-a|/2':>10}")
    print("=" * 78)

    c = (a + b) / 2
    convergio = False

    for i in range(1, n + 1):
        c  = (a + b) / 2
        fc = f(c)
        error = (b - a) / 2

        print(f"{i:>4} | {a:>12.6f} | {b:>12.6f} | {c:>12.6f} | {fc:>14.8f} | {error:>10.2e}")

        # Criterio de convergencia
        if abs(fc) < tol or error < tol:
            convergio = True
            break

        # Actualizar intervalo
        if f(a) * fc < 0:
            b = c
        else:
            a = c

    # ── Resultado ────────────────────────────────────────────
    print("=" * 78)
    if convergio:
        print(f"\n  ✔ Convergió en la iteración {i} (no tenía caso seguir).")
    else:
        print(f"\n  ⚠ Se completaron las {n} iteraciones sin converger.")
    print(f"\n  Raíz aproximada  : c    = {c:.8f}")
    print(f"  f(c)             =        {f(c):.2e}")
    print(f"  Iteraciones      :        {i}")
    print("=" * 55)


if __name__ == "__main__":
    biseccion()
