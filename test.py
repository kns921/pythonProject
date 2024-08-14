a = float(input("Введите первое значение: "))
operation = (input("Введите математический знак: "))
b = float(input("Введите второе значение: "))

if operation == "+":
    result = a + b
    print(f"Результат : {result}")


elif operation == "-":
    result = a - b
    print(f"Результат : {result}")


elif operation == "*":
    result = a * b
    print(f"Результат : {result}")


elif operation == "/":

    try:
        result = a / b
    except ZeroDivisionError:
        result = 0
        print("На ноль делить нельзя")
    print(f"Результат : {result}")

elif operation != ("+", "-", "*", "/"):
    print("Введен некорректный математический знак")
pythonpython