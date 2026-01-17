# bot.py
# Главная логика



# Импортируем TelegramAPI
from .api import TelegramAPI

# Создаем класс бота
class Bot:
    # Инициализируем класс
    def __init__(self, token: str):
        # Сохраняем API, начинаем получать обновления с самого начала
        self.api = TelegramAPI(token)
        self.offset = 0

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