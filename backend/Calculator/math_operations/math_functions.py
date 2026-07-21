import matplotlib.pyplot as plt
from sympy import symbols, plot_implicit, Eq

def calculate_expression(expression):
    x = symbols('x')
    expr = eval(expression)
    return expr.subs(x, 0)

def plot_function(expression, variable_name='x'):
    x = symbols(variable_name)
    expr = eval(expression)
    p1 = plot_implicit(Eq(expr, 0), (variable_name, -5, 5))
    plt.show()

def calculate_derivative(expression):
    x = symbols('x')
    expr = eval(expression)
    return str(expr.diff(x))

def calculate_integral(expression):
    x = symbols('x')
    expr = eval(expression)
    return str(expr.integrate(x))