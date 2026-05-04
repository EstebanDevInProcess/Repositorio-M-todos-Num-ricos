import math

def secante():
    print("=" * 55)
    print("      MÉTODO DE LA SECANTE - Búsqueda de Raíces")
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

    # ── Dos valores iniciales x0 y x1 ───────────────────────
    print("\nIngresa dos valores iniciales distintos x0 y x1:")
    while True:
        try:
            x0 = float(input("  x0 = "))
            x1 = float(input("  x1 = "))
            if x0 != x1:
                break
            print("  x0 y x1 deben ser distintos.")
        except ValueError:
            print("  Ingresa un número válido.")

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
    print("\n" + "=" * 80)
    print(f"{'Iter':>4} | {'x0':>12} | {'x1':>12} | {'x2':>12} | {'f(x2)':>14} | {'|x2-x1|':>10}")
    print("=" * 80)

    convergio = False
    x2 = x1  # por si n=0

    for i in range(1, n + 1):
        fx0 = f(x0)
        fx1 = f(x1)

        # Verificar división por cero
        if fx1 - fx0 == 0:
            print(f"\n  ✗ Error en iteración {i}: división por cero (f(x1) - f(x0) = 0).")
            print("    El método no puede continuar. Intenta con otros valores iniciales.")
            return

        # Fórmula de la secante
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fx2 = f(x2)
        error = abs(x2 - x1)

        print(f"{i:>4} | {x0:>12.6f} | {x1:>12.6f} | {x2:>12.6f} | {fx2:>14.8f} | {error:>10.2e}")

        # Criterio de convergencia
        if abs(x2 - x1) < tol or abs(fx2) < tol:
            convergio = True
            break

        # Actualizar para siguiente iteración: x0 = x1, x1 = x2
        x0 = x1
        x1 = x2

    # ── Resultado ────────────────────────────────────────────
    print("=" * 80)
    if convergio:
        print(f"\n  ✔ Convergió en la iteración {i} (no tenía caso seguir).")
    else:
        print(f"\n  ⚠ Se completaron las {n} iteraciones sin converger.")
    print(f"\n  Raíz aproximada  : x2   = {x2:.8f}")
    print(f"  f(x2)            =        {f(x2):.2e}")
    print(f"  Iteraciones      :        {i}")
    print("=" * 55)


if __name__ == "__main__":
    secante()
