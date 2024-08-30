print('Калькулятор запущен')
num_1 = input('Введите первое число: ')
while not num_1.isdigit():
    num_1 = input('Ошибка! Введите первое число еще раз: ')
num_1 = float(num_1)

num_2 = input('Введите второе число: ')
while not num_2.isdigit():
    num_2 = input('Ошибка! Введите второе число еще раз: ')
num_2 = float(num_2)

action = input('Выберите действие: "+", "-", "*", "/"')

if action == '+':
    result = num_1 + num_2
    print(f'Результат: {result}')
elif action == '-':
    result = num_1 - num_2
    print(f'Результат: {result}')
elif action == '*':
    result = num_1 * num_2
    print(f'Результат: {result}')
elif action == '/':
    try:
        result = num_1 / num_2
        print(f'Результат: {result}')
    except ZeroDivisionError:
        print('Ошибка! На ноль делить нельзя.')
else:
    print('Ошибка! Введен некорректный математический знак.')
