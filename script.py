import os
import requests

from bs4 import BeautifulSoup as BS

from time_.time_function import time_of_function

# TODO: logger for each functions

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
            response = f.read()
    except:
        response = requests.get(url)
        os.mkdir(name) if name not in os.listdir(BASE_DIR) else None
        with open(f'{name}/data.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        response = response.text
    return response


@time_of_function
def scan(data_from_url):
    """
    Работа с полученными данными: группировка расширений по их назначению.
    """
    src = BS(data_from_url, 'html.parser')
    data = src.find_all('div', class_='row mb-3')

    for table in data:
        file = table.find(
            'div',
            class_='col-12 mt-4 mb-3 font-lg font-weight-bold text-center'
        )
        expansion = table.find_all('p', class_='font-lg mb-0')

        collection = []
        for i in expansion:
            collection.append(i.text.lower())

        ALL_DATAS[file.text] = tuple(collection)
    return ALL_DATAS


@time_of_function
def sorted_files(dictonary):
    """
    Процесс сортировки по папкам.
    """
    try:
        os.mkdir('Format File')
    except:
        for file in os.listdir(BASE_DIR):
            target = file.split('.')[-1]
            for dir_, fl in dictonary.items():
                folder_name = dir_[:-1]
                if file != MAIN_FAIL.split('\\')[-1] and target in fl:
                    os.chdir('Format File')
                    if f'{folder_name}' not in os.listdir(f'{os.getcwd()}'):
                        os.mkdir(f'{folder_name}')
                    os.chdir('..')
                    os.replace(
                        src=f'{BASE_DIR}\\{file}',
                        dst=f'{BASE_DIR}\\Format File\\{folder_name}\\{file}'
                    )
        return 'done'


def main():
    task = get_data(URL)
    done = scan(task)
    print(sorted_files(done))


if __name__ == '__main__':
    main()
    main()
