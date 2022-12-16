from os import system
from random import randrange


system("cls")


def mix(some_list: list) -> list:
    res_list = []
    while len(some_list) > 0:
        res_list.append(some_list.pop(randrange(len(some_list))))
    return res_list


print("Программа реализует алгоритм перемешивания списка.\n")

# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int

while not (n := input("Введите число элементов, для генерации списка: ")).isdigit():
    print(f"\nВы ввели \"{n}\", будьте внимательнее...\n")

lt = [randrange(100) for _ in range(int(n))]

print(f"\nБыло:  {lt}")
print(f"Стало: {mix(lt[:])}\n")

while not (input("Для заверщения введите 0 и нажмите Enter, или нажмите Enter, чтобы перемешать еще раз: ") == "0"):
    print(f"\nБыло:  {lt}")
    print(f"Стало: {mix(lt[:])}\n")

print()
