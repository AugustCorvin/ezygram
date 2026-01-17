#   api.py
#   Отправка запросов в Телеграм
#   17.01.26



# Импортируем библиотеку для запросов
import requests

# Создаем класс TelegramAPI
class TelegramAPI:
    # Инициализируем класс
    def __init__(self, token: str):
        # С помощью полученного токена выстраиваем базовый URL для запросов к Телеграм
        self.base_url = f'https://api.telegram.org/bot{token}'

    # Функция запросов, принимаем метод; параметры, либо None; оставляем подсказку, что функция возвращает словарь
    def request(self, method: str, params: dict | None = None) -> dict:
        # Выстраиваем URL запроса, отправляем POST запрос и получаем ответ в JSON
        url = f'{self.base_url}/{method}'
        response = requests.post(url, json = params)
        return response.json()