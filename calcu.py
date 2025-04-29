
choice_query = int(input('Вам нужны разные комбинации вычитаний или одинаковые? (1 для одинаковых, 2 для разных): '))


def different_operators():

    expression = input('Введите операцию с выражениями (например, 9 - 7 + 3 + 9): ')
    try:

        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка в выражении: {e}"


def same_operators(n, value):
    result = value[0]
    for i in range(1, len(value)):
        if n == '+':
            result += value[i]
        elif n == '-':
            result -= value[i]
        elif n == '%':
            result %= value[i]
        elif n == '/':
            if value[i] == 0:
                return "Ошибка! Деление на ноль."
            result /= value[i]
    return result

# Основной блок выбора
if choice_query == 1:
    # Запрашиваем значения и знак для одинаковых операций
    operators = ['+', '-', '%', '/']
    n = input(f'Введите знак {operators}: ')
    value = list(map(int, input('Введите значения через пробел: ').split()))
    print("Результат одинаковых операций:", same_operators(n, value))
elif choice_query == 2:
    # В случае выбора разных операторов, сразу выполняем выражение
    print("Результат разных операций:", different_operators())
else:
    print('Ошибка, вы должны выбрать 1 или 2.')