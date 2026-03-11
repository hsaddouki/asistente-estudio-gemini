import sympy as sp
import sys

def derive_expression(expr_str, variable='x'):
    """Deriva una expresión simbólica respecto a una variable."""
    try:
        x = sp.symbols(variable)
        expr = sp.sympify(expr_str)
        derivative = sp.diff(expr, x)
        return f"Expresión: {expr}\nDerivada (d/d{variable}): {derivative}\nLaTeX: {sp.latex(derivative)}"
    except Exception as e:
        return f"Error en la derivación: {str(e)}"

def simplify_expression(expr_str):
    """Simplifica una expresión simbólica."""
    try:
        expr = sp.sympify(expr_str)
        simplified = sp.simplify(expr)
        return f"Original: {expr}\nSimplificada: {simplified}\nLaTeX: {sp.latex(simplified)}"
    except Exception as e:
        return f"Error en la simplificación: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 2:
        mode = sys.argv[1]
        content = sys.argv[2]
        if mode == "derive":
            var = sys.argv[3] if len(sys.argv) > 3 else 'x'
            print(derive_expression(content, var))
        elif mode == "simplify":
            print(simplify_expression(content))
