import pytest
from task4 import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    # Мокируем метод requests.get
    mock_get = mocker.patch('requests.get')

    # Настраиваем мок так, чтобы он возвращал успешный статус-код
    mock_get.return_value.status_code = 200

    # Настраиваем мок так, чтобы он возвращал ожидаемый JSON-ответ
    mock_get.return_value.json.return_value = [
        {'url': 'https://cdn2.thecatapi.com/images/3t6.jpg'}
    ]

    # Вызываем функцию и проверяем, что она возвращает ожидаемый URL
    cat_image_url = get_random_cat_image()
    assert cat_image_url == 'https://cdn2.thecatapi.com/images/3t6.jpg'


def test_get_random_cat_image_failure(mocker):
    # Мокируем метод requests.get
    mock_get = mocker.patch('requests.get')

    # Настраиваем мок так, чтобы он возвращал неуспешный статус-код
    mock_get.return_value.status_code = 404

    # Вызываем функцию и проверяем, что она возвращает None при неуспешном запросе
    cat_image_url = get_random_cat_image()
    assert cat_image_url is None