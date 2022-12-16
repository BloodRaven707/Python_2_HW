from os import system


system("cls")


# Можно и без проверок, если нужно просто посчитать сумму чисел в произвольной строке...
def sum_digit_in_string(some_string: str) -> int:
    res = 0

    for dig in some_string:
        if dig.isdigit():  # Просуммимует только цифры
            res += int(dig)

    return res


print("Программа принимает на вход вещественное число и показывает сумму его цифр.\n")

some = input("Введите вещественное число: ")

if some.replace("-", "", 1).replace(".", "", 1).isdigit() or some.replace("-", "", 1).replace(",", "", 1).isdigit():
    print(f"\nСумма цифр числа \"{some}\" -> {sum_digit_in_string(some)}\n")
else:
    print(f"\nК сожалению, \"{some}\", это не число, но сумма цифр в данной строке -> {sum_digit_in_string(some)}\n")
