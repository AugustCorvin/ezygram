#   __init__.py
#   Делает Bot доступным из пакета 
#   [from easygram.bot import Bot] -> [from easygram import Bot]
#   __all__ — что мы разрешаем экспортировать / команда [from easygram import *] экспортирует только то, что находится в __all__



from .bot import Bot 

__all__ = ['Bot']