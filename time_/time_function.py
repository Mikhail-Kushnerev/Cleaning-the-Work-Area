import time


def time_of_function(func):
    def wrapper(*kwargs):
        start_time = time.time()
        print(f'Запуск функции: {func.__name__}')
        result = func(*kwargs)
        execution_time = round(time.time() - start_time, 2)
        print(f'Время выполнения функции: {execution_time} c.')
        return result
    return wrapper


# @time_of_function
# def summa(a, b):
#     return a + b


# # c = time_of_function(summa)
# print(summa(2, 4))

# if __name__ == '__main__':
#     time_of_function()