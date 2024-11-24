import pytest
from mocking import get_weather

def test_get_weather(mocker):
    mock_get = mocker.patch('mocking.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description}': 'clear sky'}],
        'main' : {'temp' : 273.15}
    }

    api_key = '3f01c6c552667febfec9f22c4cef4c2d'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description}': 'clear sky'}],
        'main' : {'temp' : 273.15}
    }


def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('mocking.requests.get')
    mock_get.return_value.status_code = 404

    api_key = '3f01c6c552667febfec9f22c4cef4c2d'
    city = 'London'

    weather_data = get_weather(api_key, city)
    assert weather_data == None