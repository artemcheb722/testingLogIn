choice_query = int(input('Вам нужны разные коминации вычитаний или одинаковые: (1 - для одинаковых, 2 - для разных!): '))

def different_operators():
    value2 = input('Введите операцию с выражениями: ')
    try:
        result = eval(value2)
        return result
    except Exception as e:
        return e


def same_operators(n, value):
    value_res = value[0]
    for i in range(1, len(value)):
        if n == '+':
            value_res += value[i]
        if n == '-':
            value_res -= value[i]
        if n == '%':
            value_res %= value[i]
        if n == '/':
            value_res /= value[i]

    return value_res

if choice_query == 1:
    operators = ['+', '-', '%', '/']
    n = input(f'Введите знак {operators}: ')
    value = list(map(int, input('Введите значения:').split()))
    print("Результат одинаковых операций: ", same_operators(n, value))


elif choice_query == 2:
    print('Результат вычисления с разными операторами: ', different_operators())
else:
    print('Ошибка, вы должны ввести 1 или 2')