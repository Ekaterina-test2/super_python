def is_year_leap(number):
    return "True" if number % 4 == 0 else "Нет"


num = int(input("Введите год: "))
result = is_year_leap(num)
print(f"год {num} - {result}")
