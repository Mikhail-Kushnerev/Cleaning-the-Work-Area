import os
import requests

from progress.bar import Bar
from bs4 import BeautifulSoup as BS

from time_.sort_function import fucntion
from time_.logger import logger
from time_.time_function import time_of_function


MAIN_FAIL = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(MAIN_FAIL)
ALL_DATAS = {}
URL = 'https://www.online-convert.com/ru/file-type'


@time_of_function
def get_data(url):
    """
    Получение данных либо с файла (если он есть), либо с ссылки.
    """
    name = 'template'
    try:
        with open(f'{name}/data.html', encoding='utf-8') as f:
            response: str = f.read()
        logger.info('Файл для чтения обнаружен')
    except FileNotFoundError as file:
        logger.error(f'Файл для чтения не обнаружен \n|\t{file}')

        logger.info(f'Запрос к ресурсу {URL[8:30]}')
        response = requests.get(url)
        logger.info('Запрос к ресурсу осуществлён')

        logger.info(f'Создание директории {name}')
        os.mkdir(name)

        logger.info('Запись данных в файл')
        with open(f'{name}/data.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        logger.info(f'Директория {name} создана')

        response = response.text
    return response


@time_of_function
def scan(data_from_url):
    """
    Работа с полученными данными: группировка расширений по их назначению.
    """
    logger.info('Начинается парсинг данных')
    src = BS(data_from_url, 'html.parser')
    logger.info('Нахождение категорий')
    #! категориии для папок
    data = src.find_all('div', class_='row mb-3')

    logger.info('Парсинг расширенний для каждой категории')
    with Bar('\tРаспаковка расширений под категорию:', max=20) as bar:
        for _ in range(20):
            for table in data:
                #! название категории
                file = table.find(
                    'div',
                    class_='col-12 mt-4 mb-3 font-lg font-weight-bold text-center'
                )
                #! расширение
                expansion = table.find_all('p', class_='font-lg mb-0')
                collection = []
                for i in expansion:
                    collection.append(i.text.lower())

                ALL_DATAS[file.text] = tuple(collection)
            bar.next()
    logger.info('Данные скомплектованы')
    return ALL_DATAS


@time_of_function
def sorted_files(dictonary):
    """
    Процесс сортировки по папкам.
    """
    try:
        logger.info('Создание директории для сбору категорий')
        os.mkdir('Format File')
    except FileExistsError as file:
        logger.error(f'\n|\t{file}')
    finally:
        logger.info(f'Запуск функции {fucntion.__name__} по перемещнию файлов по папкам категорий')
        fucntion(BASE_DIR, MAIN_FAIL, dictonary)
    return '– – – –\n\tDONE'


def main():
    task = get_data(URL)
    done = scan(task)
    print(sorted_files(done))


if __name__ == '__main__':
    main()
