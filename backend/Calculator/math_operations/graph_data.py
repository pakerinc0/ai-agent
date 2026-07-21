import numpy as np
from matplotlib import pyplot as plt



# Функция для построения графика функции y = ax + b
def plot_linear_function(a, b):
    x_values = np.linspace(-10, 10, 400)
    y_values = a * x_values + b

    plt.plot(x_values, y_values, label=f'y = {a}x + {b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График линейной функции')
    plt.legend()
    plt.grid(True)
    plt.show()



# Функция для построения графика функции y = ax^2 + bx + c
def plot_quadratic_function(a, b, c):
    x_values = np.linspace(-10, 10, 400)
    y_values = a * x_values**2 + b * x_values + c

    plt.plot(x_values, y_values, label=f'y = {a}x^2 + {b}x + {c}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График квадратичной функции')
    plt.legend()
    plt.grid(True)
    plt.show()



# Функция для построения графика функции y = ax^3 + bx^2 + cx + d
def plot_cubic_function(a, b, c, d):
    x_values = np.linspace(-10, 10, 400)
    y_values = a * x_values**3 + b * x_values**2 + c * x_values + d

    plt.plot(x_values, y_values, label=f'y = {a}x^3 + {b}x^2 + {c}x + {d}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График кубической функции')
    plt.legend()
    plt.grid(True)
    plt.show()