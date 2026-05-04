import math

def punto_fijo(g, x0, max_iter, tolerancia=1e-6):
    """
    Resuelve x = g(x) por el método de punto fijo.

    Parámetros:
        g         : función g(x) tal que x = g(x)
        x0        : valor inicial
        max_iter  : número máximo de iteraciones
        tolerancia: criterio de parada (|x_nuevo - x_actual| < tolerancia)

    Retorna:
        (raiz, iteraciones_realizadas, tabla)
    """
    print(f"\n{'='*60}")
    print(f"  MÉTODO DE PUNTO FIJO")
    print(f"  x₀ = {x0} | máx. iteraciones = {max_iter} | tol = {tolerancia}")
    print(f"{'='*60}")
    print(f"{'n':>4}  {'xₙ':>18}  {'g(xₙ)':>18}  {'|error|':>14}")
    print(f"{'-'*60}")

    x = x0
    tabla = []

    for i in range(1, max_iter + 1):
        try:
            gx = g(x)
        except Exception as e:
            print(f"\n  Error evaluando g(x) en iteración {i}: {e}")
            return None, i, tabla

        if not math.isfinite(gx):
            print(f"\n  La función diverge en la iteración {i}.")
            print("  Prueba con un valor inicial x₀ diferente o reformula g(x).")
            return None, i, tabla

        error = abs(gx - x)
        tabla.append((i, x, gx, error))
        print(f"{i:>4}  {x:>18.10f}  {gx:>18.10f}  {error:>14.2e}")

        x = gx

        if error < tolerancia:
            print(f"\n  ✓ Convergió en {i} iteraciones.")
            print(f"  Raíz aproximada: x ≈ {x:.10f}")
            print(f"  Error final    : {error:.2e}")
            return x, i, tabla

    print(f"\n  ✗ No convergió en {max_iter} iteraciones.")
    print(f"  Último valor  : x = {x:.10f}")
    print(f"  Error final   : {error:.2e}")
    return x, max_iter, tabla


def pedir_funcion():
    print("\n─── MÉTODO NUMÉRICO DE PUNTO FIJO ───────────────────────")
    print("  Escribe g(x) usando sintaxis Python.")
    print("  Funciones disponibles: sin, cos, tan, sqrt, exp, log,")
    print("                         log10, pi, e")
    print("  Ejemplo: cos(x)  |  (x**2 + 2) / 3  |  sqrt(x + 2)")
    print("──────────────────────────────────────────────────────────")

    # Espacio de nombres seguro para eval
    safe_ns = {k: getattr(math, k) for k in dir(math) if not k.startswith('_')}
    safe_ns['__builtins__'] = {}

    while True:
        expr = input("\n  g(x) = ").strip()
        try:
            # Prueba rápida de sintaxis con x = 1
            test_ns = {**safe_ns, 'x': 1.0}
            eval(expr, test_ns)
            break
        except Exception as e:
            print(f"  ✗ Error en la expresión: {e}. Intenta de nuevo.")

    g = lambda x: eval(expr, {**safe_ns, 'x': x})
    return g, expr


def main():
    g, expr = pedir_funcion()

    while True:
        try:
            x0 = float(input("  Valor inicial x₀ = "))
            break
        except ValueError:
            print("  Ingresa un número válido.")
    while True:
        try:
            max_iter = int(input("  Número de iteraciones = "))
            if max_iter > 0:
                break
            print("  Debe ser mayor que 0.")
        except ValueError:
            print("  Ingresa un entero válido.")

    tol_str = input("  Tolerancia (Enter para 1e-6) = ").strip()
    try:
        tol = float(tol_str) if tol_str else 1e-6
    except ValueError:
        tol = 1e-6

    raiz, n_iter, _ = punto_fijo(g, x0, max_iter, tol)
    print(f"\n{'='*60}\n")


if __name__ == "__main__":
    main()