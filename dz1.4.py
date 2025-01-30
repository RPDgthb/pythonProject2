def print_even_reverse(n):
    for i in range(n, 0, -1):  
        if i % 2 == 0:
            print(i, end=" ")

# Приклад використання
n = int(input("Введіть число n: "))
print_even_reverse(n)