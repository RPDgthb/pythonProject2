def calculator():

    a = float(input("Введіть перше число (a): "))
    b = float(input("Введіть друге число (b): "))


    operation = input("Виберіть операцію (+, -, *, /): ")


    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            return "Ділення на нуль!"
        result = a / b
    else:
        return "Невірна операція!"

    return f"Результат: {result}"


print(calculator())