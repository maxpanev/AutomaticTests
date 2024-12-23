import unittest  # Импортирует модуль unittest для написания тестов.
from task2 import remainder  # Импортирует функцию remainder из файла task2.py.

class TestDivide(unittest.TestCase):  # Определяет тестовый класс, который наследуется от unittest.TestCase.
    def test_remainder_success(self):
        # Тестирует корректность работы функции remainder при нормальных условиях.
        self.assertEqual(remainder(8, 3), 2)  # Проверяет, что остаток от деления 8 на 3 равен 2.
        self.assertEqual(remainder(10, 2), 0)  # Проверяет, что остаток от деления 10 на 2 равен 0.
        self.assertNotEqual(remainder(10, 5), 1)  # Проверяет, что остаток от деления 10 на 5 не равен 1.

    def test_remainde_by_zero(self):
        # Тестирует функцию remainder при делении на ноль.
        self.assertRaises(ValueError, remainder, 2, 0)  # Проверяет, что при делении на ноль выбрасывается ValueError.
        # self.assertRaises(TypeError, divide, 2, 0)  # Этот тест закомментирован, и он неверен, так как divide не определена.

if __name__ == '__main__':  # Проверяет, что модуль запущен как самостоятельная программа.
    unittest.main()  # Запускает все тесты, определенные в классе TestDivide.