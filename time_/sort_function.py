import os

from progress.bar import Bar

from time_.logger import logger


def fucntion(base_dir: str, main_fail: str, dictonary: dict):
    """
        В корневой директории каждый файл смотрится на соответствии с расши-
    рением, хранящийся в словаре ALL_DATAS. В случае если это исполняемый
    файл 'script.py', то этот файл игнорируется, иной – перемещается в папку
    своей категории, лежащий в папке 'Format File'.
    """
    logger.info('Процесс сортировки')
    with Bar('|\tProcessing', max=20) as bar:
        for _ in range(20):
            for file in os.listdir(base_dir):
                target: str = file.split('.')[-1]
                for dir_, fl in dictonary.items():
                    folder_name: str = dir_[:-1]
                    if file != main_fail.split('\\')[-1] and target in fl:
                        os.chdir('Format File')
                        if f'{folder_name}' not in os.listdir(f'{os.getcwd()}'):
                            os.mkdir(f'{folder_name}')
                        os.chdir('..')
                        logger.info(f'Перемещение файла {file[:15]}')
                        os.replace(
                            src=f'{base_dir}\\{file}',
                            dst=f'{base_dir}\\Format File\\{folder_name}\\{file}'
                        )
            bar.next()
