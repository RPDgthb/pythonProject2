def factorial(n):

    if n < 0:
        return "Факторіал не визначений для негативних чисел"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result



n = int(input("Введіть число: "))
print(f"Факторіал числа {n} дорівнює: {factorial(n)}")