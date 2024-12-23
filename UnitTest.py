def check(number):
    # Проверяет, является ли число четным.
    return number % 2 == 0

def is_palindrom(s):
    # Проверяет, является ли строка палиндромом (читается одинаково в обоих направлениях).
    return s == s[::-1]

def sort_list(numbers):
    # Возвращает список чисел, отсортированный в порядке возрастания.
    return sorted(numbers)