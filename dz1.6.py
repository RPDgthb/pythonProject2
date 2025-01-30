def grade(score):
    if 0 <= score <= 49:
        return "Незадовільно"
    elif 50 <= score <= 69:
        return "Задовільно"
    elif 70 <= score <= 89:
        return "Добре"
    elif 90 <= score <= 100:
        return "Відмінно"
    else:
        return "Невірний бал"

score = int(input("Введіть кількість балів: "))
print(f"Оцінка: {grade(score)}")