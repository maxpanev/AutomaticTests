import pytest
from UnitTest import check, is_palindrom, sort_list
from PyTest import init_db, add_user, get_user

def test_check():
    # Тестирует функцию check на четное число.
    assert check(6) == True

def test_check2():
    # Тестирует функцию check на нечетное число.
    assert check(3) == False

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (5, False),
    (0, True),
    (56, True),
    (-3, False)
])
def test_check_with_param(number, expected):
    # Параметризованный тест для функции check с несколькими значениями.
    assert check(number) == expected

def test_is_palindrom_true():
    # Тестирует функцию is_palindrom на строку-палиндром.
    assert is_palindrom("madam") == True

def test_is_palindrom_false():
     #Тестирует функцию is_palindrom на строку, не являющуюся палиндромом.
    assert is_palindrom("hello") == False

@pytest.mark.parametrize("test_input, result", [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True)
])
def test_is_palindrom(test_input, result):
    # Параметризованный тест для функции is_palindrom с несколькими строками.
    assert is_palindrom(test_input) == result

def test_sort1():
    # Тестирует функцию sort_list на сортировку списка.
    assert sort_list([5, 6, 3, 1, 2]) == [1, 2, 3, 5, 6]

def test_sort2():
    # Тестирует функцию sort_list на сортировку списка с отрицательными числами.
    assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]

@pytest.fixture()
def db_conn():
    # Фикстура для создания соединения с базой данных для тестов.
    conn = init_db()
    yield conn  # Позволяет использовать соединение в тестах.
    conn.close()  # Закрывает соединение после завершения тестов.

def test_add_or_get_user(db_conn):
    # Тестирует функции add_user и get_user для добавления и извлечения пользователя.
    add_user(db_conn, "Sasha", 30)
    user = get_user(db_conn, "Sasha")
    assert user == (1, "Sasha", 30)  # Проверяет, что пользователь добавлен правильно.