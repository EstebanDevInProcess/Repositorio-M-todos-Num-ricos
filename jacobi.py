import math

# ──────────────────────────────────────────────────────────────
#  Método de Jacobi – Sistemas NO lineales (Punto Fijo)
# ──────────────────────────────────────────────────────────────
#
#  Dado un sistema de n ecuaciones, el usuario despeja cada
#  variable xᵢ en función de las demás y las ingresa como:
#       xᵢ = g_i(x1, x2, ..., xn)
#
#  El método itera:   x_nuevo[i] = g_i(x_viejo)
#  hasta que el error máximo < ε  o se agoten las iteraciones.
# ──────────────────────────────────────────────────────────────

def jacobi_nolineal():
    print("=" * 62)
    print("    MÉTODO DE JACOBI – SISTEMAS NO LINEALES")
    print("=" * 62)
    print()
    print("Debes despejar cada variable en su ecuación.")
    print()
    print("Ejemplo con 2 ecuaciones:")
    print("  Sistema:  x**2 + y - 4 = 0")
    print("            x + y**2 - 3 = 0")
    print("  Despejes: x1 = sqrt(4 - y)")
    print("            x2 = sqrt(3 - x)")
    print()
    print("Funciones disponibles: sin, cos, tan, exp, log,")
    print("                       sqrt, pi, e, abs")
    print()
    print("Nombra las variables como: x1, x2, x3, ... xn")
    print()

    # ── Número de variables ───────────────────────────────────
    n = int(input("¿Cuántas variables/ecuaciones tiene el sistema? n = "))
    nombres = [f"x{i+1}" for i in range(n)]
    print()

    # ── Ingresar las funciones de despeje g_i ─────────────────
    print("Ingresa cada despeje usando los nombres: " + ", ".join(nombres))
    print()
    g_str = []
    for i in range(n):
        expr = input(f"  Despeje de x{i+1}:  x{i+1} = ")
        g_str.append(expr)

    # Función que evalúa g_i dado el vector x actual
    def evaluar(expr, x_vals):
        contexto = {nombres[j]: x_vals[j] for j in range(n)}
        contexto.update({
            "math": math,
            "sin": math.sin,  "cos": math.cos,  "tan": math.tan,
            "exp": math.exp,  "log": math.log,  "sqrt": math.sqrt,
            "pi":  math.pi,   "e":   math.e,    "abs": abs
        })
        return eval(expr, contexto)

    # ── Aproximación inicial ──────────────────────────────────
    print()
    print("Ingresa la aproximación inicial para cada variable.")
    x0 = []
    for i in range(n):
        val = float(input(f"  Valor inicial de x{i+1}: "))
        x0.append(val)

    # ── Tolerancia ────────────────────────────────────────────
    print()
    eps = float(input("Ingresa la tolerancia ε (ej. 0.0001): "))

    # ── Número máximo de iteraciones ─────────────────────────
    max_iter = int(input("Ingresa el número máximo de iteraciones: "))

    # ── Encabezado de tabla ───────────────────────────────────
    print()
    ancho_col = 14
    sep = "-" * (6 + ancho_col * n + 2 * (n - 1) + ancho_col + 4)
    encabezado = f"{'Iter':>4}  " + "  ".join([f"{nombres[i]:>{ancho_col}}" for i in range(n)]) + f"  {'Error':>{ancho_col}}"
    print(sep)
    print(encabezado)
    print(sep)

    x      = x0[:]
    convergio  = False
    iter_count = 0
    error      = float("inf")

    for k in range(1, max_iter + 1):
        iter_count = k
        x_nuevo = [0.0] * n

        try:
            for i in range(n):
                # JACOBI: todos los g_i usan los valores del paso anterior
                x_nuevo[i] = evaluar(g_str[i], x)
        except Exception as err:
            print(f"\n  ⚠  Error al evaluar en iteración {k}: {err}")
            print("     Puede que el método haya divergido (dominio inválido).")
            break

        # Error norma infinito
        error = max(abs(x_nuevo[i] - x[i]) for i in range(n))

        vals = "  ".join([f"{x_nuevo[i]:>{ancho_col}.8f}" for i in range(n)])
        print(f"{k:>4}  {vals}  {error:>{ancho_col}.2e}")

        x = x_nuevo[:]

        if error < eps:
            convergio = True
            break

    print(sep)
    print()

    # ── Resultado ─────────────────────────────────────────────
    if convergio:
        print(f"✅  ¡Convergió en la iteración {iter_count}!")
        print(f"    Error final: {error:.2e}  <  ε = {eps}")
    else:
        print(f"⚠   Se alcanzó el máximo de {max_iter} iteraciones sin converger.")
        print(f"    Error final: {error:.2e}  (ε = {eps})")

    print()
    print("Solución aproximada:")
    for i in range(n):
        print(f"    x{i+1} = {x[i]:.10f}")
    print()

    # ── Verificación: sustituir en los despejes ───────────────
    print("Verificación (sustituir solución en cada despeje):")
    for i in range(n):
        try:
            gi_sol = evaluar(g_str[i], x)
            print(f"    g{i+1}(solución) = {gi_sol:.8f}  vs  x{i+1} = {x[i]:.8f}  "
                  f"(diff = {abs(gi_sol - x[i]):.2e})")
        except Exception:
            print(f"    g{i+1}: no se pudo evaluar.")
    print()


if __name__ == "__main__":
    jacobi_nolineal()