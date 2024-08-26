import math

#Алгоритм для нахождения максимального/минимального числа

# 1) Создаем переменную для хранения максимального элемента массива.
# 2) Перебираем весь массив, чтобы работать с каждым элементом по отдельности.
# 3) На каждом шаге сравниваем текущий элемент с переменной максимального значения. Сохраняем самый первый элемент массива в эту переменную, после чего сравниваем это значение с каждым элементом массива.
# 4) Если текущий элемент больше максимального значения, заменяем максимальное значение.
# 5) Возвращаем максимальное значение после окончания цикла.
# 6) В конце цикла получаем максимальное значение массива.

numbers = [56, 74, 23, 98, 143, -89, -23]
def find_max(list):
    # создаём переменную для хранения максимального числа в массиве
    max_number = list[0]
    for i in list:
        if i > max_number:
            max_number = i
    return max_number

print(find_max(numbers))

def find_min(list):
    # создаём переменную для хранения минимального числа в массиве
    min_number = list[0]
    for i in list:
        if i < min_number:
            min_number = i
    return min_number

print(find_min(numbers))

# Алгоритм для нахождения факториала

#5! = 1 * 2 * 3 * 4 * 5 = 120

# 1) Сравнение числа с нулем: если число равно 0, то факториал нуля будет равен 1.
# 2) Создание переменной для хранения итогового результата.
# 3) Использование цикла for и range для перебирания списка из чисел до нашего числа включительно, у которого мы ищем факториал.
# 4) Домножение результирующей переменной на текущее число в цикле.
# 5) Возврат факториала числа после цикла.

def factorial(numb):
    # проверяем, равно ли число нулю
    if numb == 0:
        return 1
    # создаём переменную для хранения результата
    result = 1
    for i in range(1, numb + 1):
        result *= i
    return result
print(factorial(7))

#Алгоритм нахождения простого цисла

# Проверяем, меньше или равно ли число 1 единице. Если да, то возвращаем false.
# Создаем цикл, перебирающий все числа от 2 до квадратного корня из нашего числа включительно (так как 2 — это первое простое число).
# Проверяем, делится ли наше число на какое-то из чисел, которые перебирает цикл, без остатка. Если да, то возвращаем false
# Существует правило: если число делится на некоторое число, большее своего квадратного корня, то оно обязательно будет делиться и на число, меньшее своего квадратного корня. Мы используем это правило, чтобы сократить количество проверок. Если число делится на любое из чисел в этом диапазоне, мы возвращаем false, так как оно не является простым.
# Если число прошло все проверки, возвращаем true

def is_prime(numbr):
    if numbr <= 1:
        return False
    for i in range(2, int(math.sqrt(numbr)) + 1):
        if numbr % i == 0:
            return False
        return True
print(is_prime(17))