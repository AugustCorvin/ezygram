# bot.py
# Главная логика



# Импортируем TelegramAPI и time
from .api import TelegramAPI
import time

# Создаем класс Message
class Message:
    def __init__(self, update):
        self.text = update['message'].get('text', '')
        self.user_id = update['message']['chat']['id']

# Создаем класс бота
class Bot:
    # Инициализируем класс
    def __init__(self, token: str):
        # Сохраняем API, начинаем получать обновления с самого начала
        self.api = TelegramAPI(token)
        self.offset = 0
        self._handlers = []   # Список функций-обработчиков

    # Декоратор для регистрации обработчиков
    def new_message(self, func):
        self._handlers.append(func)
        return func

    # Получение новых обновлений
    def get_updates(self):
        data = self.api.request('getUpdates', {'offset': self.offset + 1})

        # Если не OK, возвращаем пустой список
        if not data.get('ok'):
            return []

        # Получаем обновления
        updates = data['result']
        
        # Обновляем offset
        if updates:
            self.offset = updates[-1]['update_id']

        # Возвращаем обновления
        return updates

    # Отправка сообщений
    def send_message(self, chat_id: int, text: str):
        return self.api.request('sendMessage', {'chat_id': chat_id, 'text': text})

    # Запуск бесконечного цикла
    def run(self):
        while True:
            updates = self.get_updates()
            for update in updates:
                if 'message' in update:
                    message = Message(update)
                    for handler in self._handlers:
                        handler(message)
            time.sleep(1)