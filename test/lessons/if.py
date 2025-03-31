# age = int(input("Enter your age: "))
# if age >= 30:
#     print("You are a oldfuck.")
# elif age <= 30:
#     print("You are a teenager")

pin = 1234
print('Введите ПИН-код')

user_pin = int(input())
if user_pin == pin:
    print('Доступ разрешен')
else:
    print('Ошибка. Доступ закрыт')
    user_pin = int(input())
    if user_pin == pin:
        print('Добро пожаловать')
    else:
        print('Ошибка. Доступ закрыт, осталась 1 попытка')
        user_pin = int(input())
        if user_pin == pin:
            print('Ура, доступ открыт!')
        else:
            print('Карта заблокирована, оставайтесь на месте, за вами едет наряд мусоров...')