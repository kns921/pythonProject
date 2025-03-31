print('Для работы с калькулятором введите число')
num_1 = int(input())
try:
    var = int(num_1)
except ValueError:
    var = None

    if type (var, int):
        print('Выберите арифметическое действие')
    else:
        print('Ошибка, введите число!')
action = input()
print('Выберите 2-е число')
num_2 = int(input())

def calc(num_1, num_2):
    if action == '+':
        result = num_1 + num_2
        print('Результат: ' + str(result))
    elif action == '-':
        result = num_1 - num_2
        print('Результат: ' + str(result))
    elif action == '*':
        result = num_1 * num_2
        print('Результат: ' + str(result))
    elif action == '/':
        try:
            result = num_1 / num_2
            print('Результат: ' + result)
        except ZeroDivisionError:
            print('Ошибка на ноль делить нельзя')

calc(num_1, num_2)
