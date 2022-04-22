import time


def time_of_function(func):
    """
        Декоратор, измеряющий время работы заложенной функции. Результат
    даётся в секундаъ.
    """
    def wrapper(*args):
        start_time = time.time()
        print(f'– – – –\n| Запуск функции: {func.__name__}')
        result = func(*args)
        execution_time = round(time.time() - start_time, 2)
        print(f'| Время выполнения функции: {execution_time} c.')
        return result
    return wrapper
