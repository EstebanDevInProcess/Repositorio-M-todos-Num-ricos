import math

# ──────────────────────────────────────────────────────────────
#  Método de Gauss-Seidel – Sistemas NO lineales (Punto Fijo)
# ──────────────────────────────────────────────────────────────
#
#  Igual que Jacobi pero con una diferencia clave:
#  cada xᵢ se actualiza de inmediato y las siguientes
#  ecuaciones YA usan el valor nuevo.
#
#  Jacobi:       x_nuevo[i] = g_i(x_viejo)
#  Gauss-Seidel: x_nuevo[i] = g_i(mezcla de nuevos y viejos)
# ──────────────────────────────────────────────────────────────

def gauss_seidel():
    print("=" * 62)
    print("    MÉTODO DE GAUSS-SEIDEL – SISTEMAS NO LINEALES")
    print("=" * 62)
    print()
    print("Debes despejar cada variable en su ecuación.")
    print()
    print("Ejemplo con 2 ecuaciones:")
    print("  Sistema:  x**2 + y - 4 = 0")
    print("            x + y**2 - 3 = 0")
    print("  Despejes: x1 = sqrt(4 - x2)")
    print("            x2 = sqrt(3 - x1)")
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

    # ── Ingresar despejes g_i ─────────────────────────────────
    print("Ingresa cada despeje usando los nombres: " + ", ".join(nombres))
    print()
    g_str = []
    for i in range(n):
        expr = input(f"  Despeje de x{i+1}:  x{i+1} = ")
        g_str.append(expr)

    def evaluar(expr, x_vals):
        contexto = {nombres[j]: x_vals[j] for j in range(n)}
        contexto.update({
            "math": math,
            "sin":  math.sin,  "cos": math.cos,  "tan": math.tan,
            "exp":  math.exp,  "log": math.log,  "sqrt": math.sqrt,
            "pi":   math.pi,   "e":   math.e,    "abs": abs
        })
        return eval(expr, contexto)

    # ── Aproximación inicial ──────────────────────────────────
    print()
    print("Ingresa la aproximación inicial para cada variable.")
    x = []
    for i in range(n):
        val = float(input(f"  Valor inicial de x{i+1}: "))
        x.append(val)

    # ── Tolerancia ────────────────────────────────────────────
    print()
    eps = float(input("Ingresa la tolerancia ε (ej. 0.0001): "))

    # ── Número máximo de iteraciones ─────────────────────────
    max_iter = int(input("Ingresa el número máximo de iteraciones: "))

    # ── Encabezado de tabla ───────────────────────────────────
    print()
    ancho = 14
    sep = "-" * (6 + ancho * n + 2 * (n - 1) + ancho + 4)
    encabezado = f"{'Iter':>4}  " + "  ".join([f"{nombres[i]:>{ancho}}" for i in range(n)]) + f"  {'Error':>{ancho}}"
    print(sep)
    print(encabezado)
    print(sep)

    convergio  = False
    iter_count = 0
    error      = float("inf")

    for k in range(1, max_iter + 1):
        iter_count = k
        x_viejo = x[:]   # copia para calcular el error al final

        try:
            for i in range(n):
                # GAUSS-SEIDEL: usa x actualizado (mezcla nuevo+viejo)
                x[i] = evaluar(g_str[i], x)
        except Exception as err:
            print(f"\n  ⚠  Error al evaluar en iteración {k}: {err}")
            print("     Puede que el método haya divergido (dominio inválido).")
            break

        # Error norma infinito respecto a la iteración anterior
        error = max(abs(x[i] - x_viejo[i]) for i in range(n))

        vals = "  ".join([f"{x[i]:>{ancho}.8f}" for i in range(n)])
        print(f"{k:>4}  {vals}  {error:>{ancho}.2e}")

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

    # ── Verificación ──────────────────────────────────────────
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
    gauss_seidel()