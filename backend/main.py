import sys

def get_input():
    return input('Введите выражение: ').split()

def calculate_add(a, b):
    return float(a) + float(b)

def calculate_subtract(a, b):
    return float(a) - float(b)

def calculate_multiply(a, b):
    return float(a) * float(b)

def calculate_divide(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        print('Ошибка: Деление на ноль')
        sys.exit()

def display_result(result):
    print(f'Результат: {result}')

def main():
    while True:
        a, operator, b = get_input()
        if operator == '+':
            result = calculate_add(a, b)
        elif operator == '-':
            result = calculate_subtract(a, b)
        elif operator == '*':
            result = calculate_multiply(a, b)
        elif operator == '/':
            result = calculate_divide(a, b)
        else:
            print('Ошибка: Неверный оператор')
            continue
        display_result(result)

if __name__ == '__main__':
    main()
