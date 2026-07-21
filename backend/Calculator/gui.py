from tkinter import *
from tkinter.font import Font
from typing import List, Dict, Any, Callable
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CalculatorGUI:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Калькулятор")
        self.fonts = {
            "main": Font(family="Arial", size=14),
            "input_output": Font(family="Courier New", size=12)
        }
        
        # Создание панели с результатами
        self.result_frame = Frame(root, bg="#f0f0f0")
        self.result_entry = Entry(self.result_frame, width=30, font=self.fonts["main"])
        self.result_label = Label(self.result_frame, text="Результат:", font=self.fonts["main"], anchor=W)
        
        # Создание панели с функциями
        self.function_frame = Frame(root, bg="#f0f0f0")
        self.function_entry = Entry(self.function_frame, width=30, font=self.fonts["input_output"])
        
        # Создание кнопок для ввода цифр и операций
        self.buttons = []
        for i in range(10):
            button = Button(root, text=str(i), command=lambda x=i: self.add_to_input(x))
            self.buttons.append(button)
        
        for op in ["+", "-", "*", "/", "=", "CE"]:
            button = Button(root, text=op, command=lambda x=op: self.input_operation(x))
            self.buttons.append(button)

        # Создание кнопки для ввода функции
        self.function_button = Button(root, text="f", command=self.input_function)
        
        # Создание графического окна для отображения графиков
        self.plot_frame = Frame(root, bg="#f0f0f0")
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)

    def add_to_input(self, value: int):
        current_text = self.result_entry.get()
        if len(current_text) < 20:
            self.result_entry.insert(END, str(value))
    
    def input_operation(self, operation: str):
        current_text = self.result_entry.get()
        
        # Проверка на наличие ошибок в выражении
        try:
            result = eval(current_text)
            if isinstance(result, (int, float)):
                self.clear_input()
                self.result_entry.insert(END, result)
        except Exception as e:
            print(f"Ошибка: {e}")
    
    def input_function(self):
        pass
    
    def clear_input(self):
        self.result_entry.delete(0, END)

    def show_results(self):
        self.result_label.pack(side=LEFT)
        self.result_entry.pack(pady=5, fill=X)

    def show_functions(self):
        self.function_button.pack(pady=10)
    
    def create_buttons_grid(self):
        for i in range(3):
            for j in range(4):
                button = self.buttons.pop()
                button.grid(row=i, column=j, padx=2, pady=2)

    def show_plot(self):
        self.canvas.get_tk_widget().pack(side=TOP)
    
    def plot_function(self, function: Callable[[float], float]):
        x_values = np.linspace(-10, 10, 400)
        y_values = [function(x) for x in x_values]
        
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(x_values, y_values)
        ax.grid(True)
        self.canvas.draw()


if __name__ == "__main__":
    root = Tk()
    calc = CalculatorGUI(root)
    
    # Создание панели с результатами
    calc.result_frame.pack()
    calc.result_label.pack(side=LEFT)
    calc.result_entry.pack(pady=5, fill=X)

    # Создание панели с функциями
    calc.function_frame.pack()
    calc.function_button.pack(pady=10)

    # Создание кнопок для ввода цифр и операций
    calc.create_buttons_grid()

    root.mainloop()

