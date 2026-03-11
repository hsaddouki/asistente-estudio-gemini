import sympy as sp
from typing import Any, Dict

def compute_gradient(expression_str: str, variables: List[str]) -> Dict[str, Any]:
    """
    Calcula el gradiente simbólico de una expresión respecto a una lista de variables.
    """
    vars_sym = [sp.Symbol(v) for v in variables]
    expr = sp.sympify(expression_str)
    
    gradient = {v: sp.diff(expr, v_sym) for v, v_sym in zip(variables, vars_sym)}
    return gradient

def solve_system(equations: List[str], variables: List[str]) -> Any:
    """
    Resuelve un sistema de ecuaciones simbólicas.
    """
    vars_sym = [sp.Symbol(v) for v in variables]
    eqs_sym = [sp.sympify(eq) for eq in equations]
    
    solution = sp.solve(eqs_sym, vars_sym)
    return solution

def simplify_expression(expression_str: str) -> sp.Expr:
    """
    Simplifica una expresión matemática compleja.
    """
    expr = sp.sympify(expression_str)
    return sp.simplify(expr)

if __name__ == "__main__":
    # Ejemplo: Gradiente de Mean Squared Error (MSE)
    # MSE = (y - y_hat)^2
    grad = compute_gradient("(y - y_hat)**2", ["y_hat"])
    print(f"Gradiente MSE w.r.t y_hat: {grad}")
    
    # Ejemplo: Simplificación de la derivada de la Softmax
    # s = e^xi / sum(e^xj)
    # expr = sp.simplify("sp.exp(x) / (sp.exp(x) + sp.exp(y))")
