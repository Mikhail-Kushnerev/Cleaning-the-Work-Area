import os
from progress.bar import Bar

from time_.logger import logger


def fucntion(base_dir, main_fail, dictonary):

    logger.info('Процесс сортировки')
    with Bar('Processing', max=20) as bar:
        for _ in range(20):
            for file in os.listdir(base_dir):
                target = file.split('.')[-1]
                for dir_, fl in dictonary.items():
                    folder_name = dir_[:-1]
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
