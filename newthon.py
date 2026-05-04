import math

def derivative(f, x, h=1e-7):
    return (f(x + h) - f(x - h)) / (2 * h)

def newton_raphson():
    print("=" * 50)
    print("       Método de Newton-Raphson")
    print("=" * 50)
    print("Escribe f(x) usando sintaxis Python.")
    print("Ejemplos: x**3 - x - 2 | math.sin(x) - x/2 | math.exp(x) - 3")
    print()

    # Pedir f(x)
    while True:
        fx_str = input("f(x) = ").strip()
        try:
            f = lambda x, expr=fx_str: eval(expr, {"x": x, "math": math, "__builtins__": {}})
            f(1.0)  # prueba
            break
        except Exception as e:
            print(f"  Error en f(x): {e}. Intenta de nuevo.\n")

    # Pedir x0
    while True:
        try:
            x0 = float(input("Valor inicial x₀ = "))
            break
        except ValueError:
            print("  Ingresa un número válido.\n")

    # Pedir tolerancia
    while True:
        try:
            eps = float(input("Tolerancia ε (ej: 0.0001) = "))
            if eps <= 0:
                raise ValueError
            break
        except ValueError:
            print("  Ingresa un número positivo.\n")

    # Pedir máximo de iteraciones
    while True:
        try:
            max_iter = int(input("Máximo de iteraciones = "))
            if max_iter < 1:
                raise ValueError
            break
        except ValueError:
            print("  Ingresa un entero positivo.\n")

    print()
    print("-" * 50)
    print(f"{'Iter':>5} {'x₀':>18} {'x₁':>18} {'|Δ|':>14}")
    print("-" * 50)

    convergio = False

    for i in range(1, max_iter + 1):
        fpx0 = derivative(f, x0)

        # Verificar división por cero
        if abs(fpx0) < 1e-14:
            print(f"\n  ✗ Error: f′(x₀) ≈ 0 en x₀ = {x0:.8f} → División por cero.")
            break

        x1 = x0 - f(x0) / fpx0
        delta = abs(x1 - x0)

        print(f"{i:>5} {x0:>18.8f} {x1:>18.8f} {delta:>14.2e}")

        # Verificar convergencia
        if delta < eps:
            convergio = True
            print("-" * 50)
            print(f"\n  ✓ Convergió en la iteración {i}")
            print(f"  Raíz aproximada: x ≈ {x1:.10f}")
            print(f"  f(x₁) = {f(x1):.2f}")
            print(f"  Error final |Δ| = {delta:.2e} < ε = {eps}")
            break

        x0 = x1
    else:
        print("-" * 50)
        print(f"\n  ✗ No convergió en {max_iter} iteraciones.")
        print(f"  Último x₁ = {x0:.10f}")

    print("=" * 50)

if __name__ == "__main__":
    newton_raphson()