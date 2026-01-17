from .api import TelegramAPI   # TelegramAPI
import time                    # Управление задержкой



class Message:
    def __init__(self, update):
        self.text = update['message'].get('text', '')   # Получаем текст сообщения
        self.user_id = update['message']['chat']['id']  # получаем ID отправителя


class Bot:
    # Инициализация
    def __init__(self, token: str):
        self.api = TelegramAPI(token)   # сохраняем API
        self.offset = 0                 # начинаем получать обновления с самого начала
        self._handlers = []             # список функций-обработчиков

    # Декоратор для регистрации обработчиков
    def new_message(self, func):
        self._handlers.append(func)     # добавляем функцию
        return func                     # возвращает функцию

    # Получение новых обновлений
    def get_updates(self):
        data = self.api.request('getUpdates', {'offset': self.offset + 1})
        if not data.get('ok'):          # Если вернулось не 'ok'
            return []                   # возвращаем пустой список

        # Получаем обновления
        updates = data['result']
        if updates:                     # обновляем offset
            self.offset = updates[-1]['update_id']
        return updates                  # возвращаем обновления

    # Отправка сообщений
    def send_message(self, chat_id: int, text: str):
        return self.api.request('sendMessage', {'chat_id': chat_id, 'text': text})

    # Запуск бесконечного цикла
    def start(self):
        while True:                                 # вечно проверяем обновления
            updates = self.get_updates()

            for update in updates:                  # обрабатываем обновления

                if 'message' in update:             # если это сообщение
                    message = Message(update)       # создаем объект message
                    for handler in self._handlers:  # перебираем все функции
                        handler(message)            # вызываем функцию с объектом message
            time.sleep(1)                           # Спим 1 секунду