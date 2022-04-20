# Cleaning the Work Area

Скрипт, чистящий рабочую зону проекта – файлы с разными расширениями  
перемещаются под соответсвующие папки:  
- `html` -> `Website`
- `py` -> `Developer`  

и т.д.

## Оглавление

- [Технологии](#технологии)
- <a href="#t1"> Структура проекта </a>
- [Описание работы скрипта](#описание-работы)
- [Авторы](#авторы)

## Технологии

- Python 3.10
- BeautifulSoup

[⬆️Оглавление](#оглавление)

<details>
  <summary>
      <h2 id="t1"> Структура проекта </h2>
  </summary>

```cmd
Cleaning the Work Area
|   .gitignore
|   README.md
|   script.py  <-- Исполняемый файл
|
+---Format File  <-- Папка, где будут созданы папки для разных расширений
|   +---Developer
|   +---Document
|   +---Raster image
|   \---Website
|   ...
|
+---template  <-- Папка, где лежит html страница ресурса
|       data.html
|
\---time_  <-- Собственный модуль, для измерения времени работы функции
    |   time_function.py
```

</details>

[⬆️Оглавление](#оглавление)

## Описание работы

Скрипт, с помощью функции `get_data`, обращается к ресурсу  
`https://www.online-convert.com/ru/file-type`, обладающий большой базой  
расширений, сохраняет **html**-страницу в файл `data.html`, локализация  
которого продемонстрирована в  <a href="#t1"> дереве проекта </a>. При  
парсинге страницы (функция `scan`) данные (расширения, область сферы)  
сохраняются в словаре **ALL_DATAS**:

```py
{
    'Archive:': ('zip', 'rar', ...),
    'Audio:': ('mpc', 'aac', ...),
    'CAD:': ('dxf', 'dwg', ...),
    'Data:': ('dif', 'vcf', ...),
    ...
}
```

Имея все данные, происходит сортировка расширений по папкам с помощью  
функции `sorted_files`. Итоговый результат по факту работы сортировки  
продемонстрирован так же в <a href="#t1"> дереве проекта </a>

[⬆️Оглавление](#оглавление)

## Авторы

[**Mikhail Kushnerev**](https://github.com/Mikhail-Kushnerev)  
[⬆️в начало](#cleaning-the-work-area)
