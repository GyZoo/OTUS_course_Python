"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    return [number ** 2 for number in numbers]
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return number > 1


def filter_numbers(numbers, type):
    if type == ODD:
        return [number for number in numbers if number % 2 != 0] #
    elif type == EVEN:
        return [number for number in numbers if number % 2 == 0]
    elif type == PRIME:
        return list(filter(is_prime, numbers))

    
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
