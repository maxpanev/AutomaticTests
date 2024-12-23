import requests


def get_random_cat_image():
    # URL для запроса к API, который возвращает случайное изображение кошки
    url = 'https://api.thecatapi.com/v1/images/search'

    # Выполняем GET-запрос к указанному URL
    response = requests.get(url)

    # Если запрос прошел успешно (статус код 200)
    if response.status_code == 200:
        # Преобразуем ответ в JSON-формат
        data = response.json()

        # Проверяем, что данные не пустые и содержат ключ 'url'
        if data and 'url' in data[0]:
            # Возвращаем URL изображения кошки
            return data[0]['url']

    # Возвращаем None, если запрос не был успешным или данные не содержат ключ 'url'
    return None