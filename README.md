# Cleaning the Work Area

Скрипт, чистящий рабочую зону проекта – файлы с разными расширениями  
перемещаются под соответсвующие папки:  
- `html` -> `Website`
- `py` -> `Developer`
и т.д.

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
\---time_
    |   time_function.py
```

</details>

Скрипт обращается к ресурсу `https://www.online-convert.com/ru/file-type`,  
обладающий большой базой расширений, и сохраняет спарсенные данные  
(расширения, область сферы) в файл `data.html`, локализация которого  
продемонстрирована в <a href="#t1"> дереве проекта </a>
