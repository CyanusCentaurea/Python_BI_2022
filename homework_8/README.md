# Python_BI_2022
**Python_BI_2022** - это публичный репозиторий для работы с домашними заданиями по Python в Институте биоинформатики.
## homework_1
Реализована программа, которая в бесконечном цикле считывает команды от
пользователя. После команды программа запрашивает у пользователя
последовательность нуклеиновой кислоты и распечатывает результат.

**Список команд:**

*exit* — завершение исполнения программы

*transcribe (t)* — напечатать транскрибированную последовательность

*reverse (r)* — напечатать перевёрнутую последовательность

*complement (c)* — напечатать комплементарную последовательность

*reverse complement (rc)* — напечатать обратную комплементарную последовательность


* Программа сохраняет регистр символов (например, complement AtGc это TaCg).
* Программа сообщает пользователю об ошибках при вводе некорректных команд и последовательностей, даёт возможность исправлять запрос, пока он не будет правильным.
* Программа работает только с последовательностями нуклеиновых кислот. К примеру, последовательность AUTGC не может существовать, так как содержит T и U, такие случаи нужно обрабатывать и сообщать об этом пользователю.
* Программа не использует сторонние модули.
## homework_2
Реализована программа fastq_filtrator.py для работы с fastq файлами.

**Программа умеет:**

1. Фильтровать риды по GC составу
2. Фильтровывать риды по качеству
3. Фильтровать риды по длине
4. Сохранять результаты в файл

**В программе реализована функция main, которая принимает следующие аргументы:**
1. *input_fastq* - путь к файлу, который подаётся на вход программе (обычный не сжатый fastq файл).
2. *output_file_prefix* - префикс пути к файлу, в который будет записан результат. К префиксу прибавляется "_passed.fastq" для файла с ридами, прошедшими фильтрацию и "_failed.fastq" для файлов и отфильтрованными ридами (только если аргумент save_filtered равен True).
3. *gc_bounds* - интервал GC состава (в процентах) для фильтрации ***(по умолчанию равен (0, 100)***, т. е. все риды сохраняются). Если в аргумент передать одно число, то считается, что это верхняя граница. Примеры: gc_bounds = (20, 80) - сохраняем только риды с GC составом от 20 до 80%, gc_bounds=44.4 - сохраняем риды с GC составом не более чем 44.4%.
4. *length_bounds* - интервал длины для фильтрации, всё аналогично gc_bounds, но ***по умолчанию равен (0, 2\*\*32)***.
5. *quality_threshold* - пороговое значение среднего качества рида для фильтрации, ***по умолчанию равно 0 (шкала phred33)***. Риды со средним качеством по всем нуклеотидам ниже порогового отбрасываются.
6. *save_filtered* - сохранять ли отфильтрованные риды, ***по умолчанию равен False***.

Все описанные интервалы включают и верхнюю, и нижнюю границы.

Программа не использует сторонние модули.
## homework_3
Программист Михаил крайне заинтересовался темой виртуальных окружений и решил исследовать её поподробнее. После долгих лет исследований он решил опубликовать статью и даже приложил к ней код на гитхабе (https://github.com/krglkvrmn/Virtual_environment_research). Михаил утверждает, что любой человек может с лёгкостью воспроизвести его результаты. Вы, как человек очень заинтересованный в теме, тоже решили воспроизвести результаты исследования. Однако на практике оказалось, что код Михаила совершенно не адаптирован для запуска другими людьми. И куда смотрели рецензенты? Журнал-то очень высокоимпактный... В итоге пришлось чинить всё самостоятельно.

1. Подобраны необходимые зависимости для успешного запуска скрипта ultraviolence.py.
2. Создан файл requirements.txt, содержащий список всех необходимых сторонних библиотек питона для запуска этого скрипта.
3. Файл ultraviolence.py не редактировался.
5. В файле requirements.txt минимальное количество лишних зависимостей.


## How to run ultraviolence.py: 
**tested with**
* Ubuntu 22.04
* pip 22.3
* setuptools 63.2.0
* Python 3.11.0rc2    
    
pip - the package installer for Python installation    
`$ sudo apt install python3-pip`    
     
To run the ultraviolence script.py you need Python version 3.11, which is not available in the official repositories of Ubuntu 22.04 at the time of writing the manual (17.10.2022). You can use the independent repository deadsnakes to install Python3.11.  
          
Install managing software for apt repositories:   
`$ sudo apt install software-properties-common`     
     
add ppa repository (personal package archive):   
`$ sudo add-apt-repository ppa:deadsnakes/ppa`      
       
Now you can install Python 3.11:   
`$ sudo apt install python3.11 python3.11-dev`   
> We recommend to use separate virtual environment for the project to avoid conflicts of installed modules.    
>    
> Install Python3.11 package to work with the virtual environment    
> `$ sudo apt install python3.11-venv`     
>             
> Create a virtual environment...        
> `$ python3.11 -m venv environment`     
>  
> ...and activate it:     
> `$ source environment/bin/activate`  
    
Installing modules without unnecessary dependencies:
you can install modules from requirements.txt   
`$ pip install -r requirements.txt`   
    
or manually     
`$ pip install --upgrade --no-deps google-api-python-client beautifulsoup4 requests urllib3 charset_normalizer idna certifi biopython aiohttp multidict attrs yarl async_timeout aiosignal frozenlist six pandas numpy pytz python-dateutil opencv-python lxml`    
    
Solving "ValueError: index cannot be a set" of the Pandas module:
`$ sed -i '636s/^/#/' /your_path_to_lib/python3.11/site-packages/pandas/core/frame.py; sed -i '637s/^/#/' /your_path_to_lib/python3.11/site-packages/pandas/core/frame.py`       
for example:      
`$ sed -i '636s/^/#/' /home/oxana/environment/lib/python3.11/site-packages/pandas/core/frame.py; sed -i '637s/^/#/' /home/oxana/environment/lib/python3.11/site-packages/pandas/core/frame.py`     

### Good job! Now you can run ultraviolence.py!
## homework_4
Реализована программа numpy_challenge.py для работы с библиотекой NumPy.

**В программе реализованы следующие функции:**
1. *array_build*, создаёт 3 различных эррея разными способами.
2. *matrix_multiplication*, принимает 2 матрицы, перемножает их по соответствующим правилам матричного перемножения и выдаёт получившуюся матрицу.
3. *multiplication_check*, принимает список с матрицами и выдаёт True, если они могут быть перемножены друг на друга в порядке, в котором они находятся в списке, и False, если их нельзя перемножить.
4. *multiply_matrices*, принимает список с матрицами и выдаёт результат перемножения, если его можно получить, или возвращает None, если их нельзя перемножить.
5. *compute_2d_distance*, принимает 2 одномерных эррея c парой значений (как координаты точки на плоскости) и вычисляет расстояние между ними.
6. *compute_multidimensional_distance*, принимает 2 одномерных эррея с любым количеством значений (но равным) и вычисляет расстояние между ними.
7. *compute_pair_distances*, принимает 2d эррей, где каждая строка это наблюдение, а каждый столбец - фича. Рассчитывает и возвращает матрицу попарных расстояний.

Программа использует библиотеку NumPy 
Программа использует библиотеку NumPy, Вы можете установить ее с помощью файла requirements.txt командой       
`$ pip install -r requirements.txt`
## homework_5
### Работа с реальными данными
В форматах .py и .ipynb реализована программа hw_5_pandas_visualizations для работы с Pandas, matplotlib и seaborn.     
**В программе реализованы следующие функции:**
1. *read_gff* для чтения файлов в .gff формате;      
2. *read_bed6* для чтения файлов в .bed6 формате.    

* В полученном с помощью функции read_bed6 дата фрейме alignment обработана колонка attributes таким образом, что в ней остались только данные о типе рРНК одной короткой строкой (16S, 23S, 5S).      
* Выведена таблица, где для каждой хромосомы показано количество рРНК каждого типа.      
* Построен barplot, отображающий эти данные.    
* Для получения информации о количестве успешно собранных рРНК выведена таблица, содержащая исходные записи об рРНК, полностью вошедших в сборку, а также запись о контиге в который попала указанная РНК (аналогия с работой команды bedtools intersect).
* Максимально точно воспроизведен заданный график volcano_plot по данным diffexpr_data.tsv.gz.
* Построены различные графики на основе датасета по COVID-19 (owid-covid-data.tsv), выдвинуты гипотезы, сделаны некоторые выводы.

### How to run hw_5_pandas_visualizations.ipynb:

> We recommend to use separate virtual environment for the project to avoid conflicts of installed modules.    
>    
> Install Python3.11 package to work with the virtual environment    
> `$ sudo apt install python3.11-venv`     
>             
> Create a virtual environment...        
> `$ python3.11 -m venv environment`     
>  
> ...and activate it:     
> `$ source environment/bin/activate` 

You can install modules from requirements.txt     
`$ pip install -r https://github.com/CyanusCentaurea/Python_BI_2022/blob/homework_5/homework_5/requirements.txt`

Install jupyter:      
`$ pip install jupyter`

Using the command `cd` move to the directory in which you are planning to work.  
        
Then run jupyter with command      
`$ jupyter notebook`

This will start the Jupyter server and your browser will open a new tab where you can open and run the script.     

## homework_6
Реализована программа regexp_hw.py для работы с регулярными выражениями в Python.

1. Программа парсит файл references.txt при помощи регулярных выражений и записывает все ftp ссылки из него в файл ftps.txt. Всего в файле references.txt программа обнаружила **12850** ftp ссылок.  
2. Программа извлекает из рассказа 2430 A.D. (файл 2430 A.D.txt) все числа и выводит их на экран. Всего в тексте программа обнаружила **11** чисел.
3. Программа извлекает из рассказа 2430 A.D. (файл 2430 A.D.txt) все слова, в которых есть буква a, регистр при этом не важен. Всего в тексте программа обнаружила **985** слов с буквой a.
4. Программа извлекает из рассказа 2430 A.D. (файл 2430 A.D.txt) все восклицательные предложения. Всего в тексте программа обнаружила **6** восклицательных предложений.
5. Построены три гистограммы распределения длин уникальных слов (без учёта регистра, длина от 1) в рассказе 2430 A.D. (файл 2430 A.D.txt).    
* По оси x в первой гистограмме отложена длина слова. По оси y отложено количество слов с такой длиной, найденное в тексте. Регистр при этом не важен.        
* По оси x во второй гистограмме отложена длина слова. По оси y отложена доля слов с такой длиной среди уникальных слов, найденных в тексте. Регистр при этом не важен.        
* По оси x во второй гистограмме отложена длина слова. По оси y отложена доля слов (в процентах) с такой длиной среди уникальных слов, найденных в тексте. Регистр при этом не важен.   

**В программе реализованы следующие функции:**
1. *brick_language*, осуществляет перевод русского текста, переданного в качестве агрумента, на кирпичный язык.   

> **Кирпичный язык**: после каждой гласной буквы в слове добавляется буква 'c' и эта гласная буква.
> Например, словосочетание *"По бревну бобры бредут"* на кирпичном языке будет звучать так: *"Посо бресевнусу бособрысы бреседусут"*.

2. *find_n_words_sentences*, принимает 2 аргумента: текст в виде строки и количество слов в предложении. Возвращает список кортежей, каждый из которых содержит отдельные слова из найденных предложений.

### How to run regexp_hw.py:

> We recommend to use separate virtual environment for the project to avoid conflicts of installed modules.    
>    
> Install Python3.11 package to work with the virtual environment    
> `$ sudo apt install python3.11-venv`     
>             
> Create a virtual environment...        
> `$ python3.11 -m venv environment`     
>  
> ...and activate it:     
> `$ source environment/bin/activate`      
> You can install modules from requirements.txt         
> `$ pip install -r https://github.com/CyanusCentaurea/Python_BI_2022/blob/homework_6/homework_6/requirements.txt`       
> Now you can run regexp_hw.py:      
> `$ python3.11 regexp_hw.py`

## homework_7
Реализована программа functional.py.     
**В программе реализованы следующие функции:**
1. *sequential_map* - принимает в качестве аргументов любое количество функций (позиционными аргументами, НЕ списком), а также контейнер с какими-то значениями в качестве последнего позиционного аргумента. Функция возвращает список результатов последовательного применения переданных функций к значениям в контейнере.          
> Например, sequential_map(np.square, np.sqrt, lambda x: x\*\*3, [1, 2, 3, 4, 5]) -> [1.0, 8.0, 27.0, 64.0, 125.0]      

2. *consensus_filter* - принимает в качестве аргументов любое количество функций (позиционными  аргументами, НЕ списком), возвращающих True или False, а также контейнер с какими-то значениями в качестве последнего позиционного аргумента. Функция возвращает список значений, которые при передаче их во все функции дают True.         
> Например: consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11]) -> [6]     

3. *conditional_reduce* - принимает 2 функции, а также контейнер с значениями. Первая функция принимает 1 аргумент и возвращает True или False, вторая также принимает 2 аргумента и возвращает значение (как в обычной функции reduce). conditional_reduce возвращает одно значение - результат reduce, пропуская значения, с которыми первая функция выдала False.         
> Например, conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]) -> 4      

4. *func_chain* - принимает в качестве аргументов любое количество функций (позиционными  аргументами, НЕ списком). Функция возвращает функцию, объединяющую все переданные последовательным выполнением.         
> Например, my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4)). my_chain(37) -> (9.75, 9)      

5. *my_print* - полный аналог функции *print* (без аргумента flush).      

## homework_8
Реализованы упрощенные аналоги утилит wc, ls, sort, rm, grep, cat, tail, mkdir, cp, mv, uniq.     

> Рекомендуется работать в отдельном окружении во избежание возникновения конфликтов между установленными модулями.     
>    
> Установите Python3.11 для работы с виртуальным окружением:    
> `$ sudo apt install python3.11-venv`     
>             
> Создайте виртуальное окружение...        
> `$ python3.11 -m venv environment`     
>  
> ...и активируйте его:     
> `$ source environment/bin/activate`      

После этого можно запускать программы. Обратите внимание на примеры использования каждой "утилиты", приведенные ниже.    

1. **wc.py**     
 
*использование*: ./wc.py [-h] [-c] [-l] [-w] [files ...]

Упрощенный аналог утилиты wc <https://www.gnu.org/software/coreutils/wc>.    
Печатает число символов новой строки, слов и байт для каждого ФАЙЛА и      
итоговую строку, если было задано несколько ФАЙЛОВ. Словом считается      
последовательность символов ненулевой длины, отделённая пробельным символом.     

Если ФАЙЛ не задан, читает стандартный ввод (с завершением через Ctrl + D).    

Для выбора выводимых счётчиков используются следующие параметры      
(счётчики всегда выводятся в таком порядке: символы новой строки,     
слова, байты).       

позиционные аргументы:      
  files        файлы для обработки      

опциональные аргументы:        
  -h, --help   показать эту справку и выйти    
  -c, --bytes  напечатать количество байт   
  -l, --lines  напечатать количество новых строк    
  -w, --words  напечатать количество слов     

*примеры использования*

> `$ echo 'hello world' | ./wc.py`   
> 1 2 12   
>   
> `$ ./wc.py -l`   
> hello world!   
> Linux   
> Unix   
> 3    
>   
> `$ echo 'Hello from file1.txt!' > file1.txt`   
>   
> `$ echo 'Hello from file2.txt!' > file2.txt`  
>  
> `$ echo 'Hello from file3.txt!' > file3.txt`          
>
> `$ ./wc.py -c *.txt`   
> 22 file1.txt    
> 22 file2.txt   
> 22 file3.txt   
> 66 total   
>
> `$ ./sort.py file1.txt file2.txt file3.txt | ./uniq.py | ./wc.py`   
> 3 9 66    

2. **ls.py**     
 
*использование*: ./ls.py [-h] [-a] [paths ...]

Упрощенный аналог утилиты ls <https://www.gnu.org/software/coreutils/ls>.   
Выдаёт информацию о ФАЙЛАХ (по умолчанию в текущем каталоге).   

позиционные аргументы:   
  paths       пути директорий для обработки   

опциональные аргументы:   
  -h, --help  показать эту справку и выйти   
  -a, --all   не скрывать файлы начинающиеся с .     

*примеры использования*   
 
> `$ echo 'Hello from file1.txt!' > file1.txt`   
>   
> `$ echo 'Hello from file2.txt!' > file2.txt`  
>  
> `$ echo 'Hello from file3.txt!' > file3.txt`          
>
> `$ ./ls.py | ./sort.py | ./uniq.py`   
> Python_BI_2022 file1.txt file2.txt file3.txt    
> 
> `$ ./ls.py`    
> Python_BI_2022 file1.txt file2.txt file3.txt      
>   
> `$ ./mkdir.py -p ./TEST1/TEST2/TEST3`     
>
> `$ ./cp.py file1.txt ./TEST1/TEST2/` 
> 
> `$ ./ls.py ./TEST1/TEST2/`    
> TEST3 file1.txt
> `$ ./ls.py / | ./wc.py -c`
> 119

3. **sort.py**     
 
*использование*: ./sort.py [-h] [files ...]

Упрощенный аналог утилиты sort <https://www.gnu.org/software/coreutils/sort>.     
Печатает сортированное слияние всех ФАЙЛ(ов) на стандартный вывод.   
Если ФАЙЛ не задан, читает стандартный ввод (с завершением через Ctrl + D).       

позиционные аргументы:      
  files        файлы для обработки      

опциональные аргументы:        
  -h, --help   показать эту справку и выйти        

*примеры использования*    

> `$ ./sort.py`    
> Unix   
> Linux   
> Windows   
>   
> Linux   
> Unix   
> Windows  
> 
>   
> `$ echo 'Hello from file1.txt!' > file1.txt`   
>   
> `$ echo 'Hello from file2.txt!' > file2.txt`  
>  
> `$ echo 'Hello from file3.txt!' > file3.txt`            
>
> `$ ./sort.py *.txt | ./uniq.py | ./wc.py`   
> 3 9 66 
     
4. **rm.py**     
 
*использование*: ./rm.py [-h] [-r] [files ...]

Упрощенный аналог утилиты rm <https://www.gnu.org/software/coreutils/rm>.     
Удаляет ФАЙЛ(ы).     

позиционные аргументы:      
  files        файлы для обработки      

опциональные аргументы:        
  -h, --help   показать эту справку и выйти        
  -r, --recursive  рекурсивно удалить каталоги и их содержимое  
  
*примеры использования*    
   
> `$ echo 'Hello from file1.txt!' > file1.txt`   
>   
> `$ echo 'Hello from file2.txt!' > file2.txt`  
>  
> `$ echo 'Hello from file3.txt!' > file3.txt`    
> 
> `$ ./mkdir.py -p ./TEST1/TEST2/TEST3`        
>  
> `$ ./ls.py`   
> Python_BI_2022 TEST1 file1.txt file2.txt file3.txt   
>   
> `$ ./rm.py -r TEST1`     
>   
> `$ ./ls.py`   
> Python_BI_2022 file1.txt file2.txt file3.txt   
>    
> `$ ./rm.py *.txt`   
> 
> `$ ./ls.py`   
> Python_BI_2022

5. **grep.py**     
 
*использование*: ./grep.py [-h] pattern [files ...]

Упрощенный аналог утилиты grep <https://www.gnu.org/software/coreutils/grep>.      
Поиск ШАБЛОНОВ (pattern) в каждом ФАЙЛЕ.    
Выводит строки, в которых найдены совпадения с шаблоном.     
Если ФАЙЛ не задан, читает стандартный ввод (с завершением через Ctrl + D).    

позиционные аргументы:      
  files        файлы для обработки      

опциональные аргументы:        
  -h, --help   показать эту справку и выйти         
  
*примеры использования*    
  
> `$ echo 'Hello from file1.txt!' > file1.txt`   
>   
> `$ echo 'Hello from file2.txt!' > file2.txt`  
>  
> `$ echo 'Hello from file3.txt!' > file3.txt`      
>   
> `$ ./grep.py Hello *.txt`     
> file1.txt:Hello from file1.txt!    
> file2.txt:Hello from file2.txt!   
> file3.txt:Hello from file3.txt!   
>   
> `$ ./grep.py Linux`     
> Hello    
> Unix   
> Linux   
> Linux  
> WindowsLinux  
> WindowsLinux   
>  
> `$ ./ls.py | ./sort.py | ./grep.py file`  
> Python_BI_2022 file1.txt file2.txt file3.txt 

6. **cat.py**     
 
*использование*: ./cat.py [-h] [files ...]

Упрощенный аналог утилиты cat <https://www.gnu.org/software/coreutils/cat>.     
Печатает слияние ФАЙЛ(ов) на стандартный вывод.
Если ФАЙЛ не задан, читает стандартный ввод (с завершением через Ctrl + D).       

позиционные аргументы:      
  files        файлы для обработки      

опциональные аргументы:        
  -h, --help   показать эту справку и выйти        

*примеры использования*    
 
> `$ echo 'Hello from file1.txt!' > file1.txt`   
>   
> `$ echo 'Hello from file2.txt!' > file2.txt`  
>  
> `$ echo 'Hello from file3.txt!' > file3.txt`            
>
> `$ ./sort.py *.txt | ./uniq.py | ./wc.py` 
>      
> `$ ./cat.py file1.txt file2.txt file3.txt`    
> Hello from file1.txt!    
> Hello from file2.txt!    
> Hello from file3.txt!  
>      
> `$ ./cat.py`   
> Windows   
> Windows   
> Linux   
> Linux   
> Unix  
> Unix   

7. **tail.py**     
 
*использование*: ./tail.py [-h] [-n LINES] [files ...]

Упрощенный аналог утилиты tail <https://www.gnu.org/software/coreutils/tail>.     
Печатает последние 10 строк каждого из ФАЙЛОВ на стандартный вывод.
Если задано несколько ФАЙЛОВ, сначала печатает заголовок с именем файла.

Если ФАЙЛ не задан, читает стандартный ввод (с завершением через Ctrl + D).  

позиционные аргументы:      
  files        файлы для обработки      

опциональные аргументы:        
  -h, --help   показать эту справку и выйти        
  -n LINES, --lines LINES  выводить последние LINES строк, а не последние 10
  
*примеры использования*    
   
> `$ ./tail.py file4.txt`  
>    
> \=\=> file4.txt <\=\=    
> Hello from line3 of test4.txt!      
> Hello from line4 of test4.txt!    
> Hello from line5 of test4.txt!    
> Hello from line6 of test4.txt!    
> Hello from line7 of test4.txt!    
> Hello from line8 of test4.txt!   
> Hello from line9 of test4.txt!   
> Hello from line10 of test4.txt!   
> Hello from line11 of test4.txt!   
> Hello from line12 of test4.txt!   
> `$ ./tail.py -n 5`     
> line1    
> line2     
> line3     
> line4    
> line5    
> line6     
> line7  
>   
> line3    
> line4     
> line5    
> line6   
> line7     
> `$ ./tail.py -n 1 file1.txt file2.txt file3.txt`     
> \=\=> file1.txt <\=\=    
> Hello from file1.txt!   
> \=\=> file2.txt <\=\=   
> Hello from file2.txt!   
> \=\=> file3.txt <\=\=   
> Hello from file3.txt!  
>   
> `$ ./ls.py | ./tail.py`   
> Python_BI_2022 file1.txt file2.txt file3.txt 

8. **mkdir.py**     
 
*использование*: ./mkdir.py [-h] [-p] [files ...]

Упрощенный аналог утилиты mkdir <https://www.gnu.org/software/coreutils/mkdir>.     
Создает каталог(и).     

позиционные аргументы:      
  files        каталоги для создания      

опциональные аргументы:        
  -h, --help   показать эту справку и выйти        
  -p, --parents  не выдавать ошибку, если существует; создавать
                 родительские каталоги при необходимости  
  
*примеры использования*    
   
> `$ ./ls.py`   
> Python_BI_2022 
>   
> `$ ./mkdir.py TEST1`  
>    
> `$ ./ls.py`   
> Python_BI_2022 TEST1
>  
> `$ ./mkdir.py TEST1/TEST2/TEST3`      
> mkdir: cannot create directory «TEST1/TEST2/TEST3»: No such file or directiry
>  
> `$ ./mkdir.py -p TEST1/TEST2/TEST3`        
>   
> `$ ./ls.py`   
> Python_BI_2022 TEST1  

9. **cp.py**     
 
*использование*: ./cp.py [-h] [-p] [files ...]

Упрощенный аналог утилиты cp <https://www.gnu.org/software/coreutils/cp>.     
Копирует ИСТОЧНИК в НАЗНАЧЕНИЕ, или несколько ИСТОЧНИКОВ в КАТАЛОГ.    

позиционные аргументы:      
	src              источник(и)
	dst              назначение     

опциональные аргументы:        
  -h, --help   показать эту справку и выйти        
  -r, --recursive  рекурсивно удалить каталоги и их содержимое  
  
*примеры использования*    
   
> `$ ./cp.py file1.txt TEST1 | ./ls.py TEST1`      
> TEST2 file1.txt    
>
> `$ cp -r TEST1 TEST2 | ./ls.py TEST2`     
> TEST2 file1.txt     

10. **mv.py**     
 
*использование*: ./mv.py [-h] src [src ...] dst

Упрощенный аналог утилиты mv <https://www.gnu.org/software/coreutils/mv>.     
Переименовывает ИСТОЧНИК в НАЗНАЧЕНИЕ, или перемещает ИСТОЧНИК(и) в КАТАЛОГ.    

позиционные аргументы:      
	src              источник(и)
	dst              назначение     

опциональные аргументы:        
  -h, --help   показать эту справку и выйти        
  
*примеры использования*    

> `$ ./ls.py`     
> Python_BI_2022 TEST1     
>   
> `$ ./mv.py TEST1 TEST2 | ./ls.py`     
> Python_BI_2022 TEST2    
>
> `$ cp -r TEST1 TEST2 | ./ls.py TEST2`    
> TEST2 file1.txt
>   
> `$ echo 'Hello from file1.txt!' > file1.txt`   
>   
> `$ echo 'Hello from file2.txt!' > file2.txt`   
>  
> `$ echo 'Hello from file3.txt!' > file3.txt`    
>
> `$ ./ls.py`  
> Python_BI_2022 TEST1 file1.txt file2.txt file3.txt     
>  
> `$ ./mv.py file1.txt file2.txt file3.txt TEST2 | ./ls.py TEST2`   
> TEST2 file1.txt file2.txt file3.txt     

11. **uniq.py**     
 
*использование*: ./uniq.py [-h] [files ...]

Упрощенный и модифицированный аналог утилиты uniq <https://www.gnu.org/software/coreutils/uniq>.     
Фильтрует все совпавшие строки из ВХОДА (или стандартного ввода),
записывая их в ВЫХОД (или стандартный вывод).

Без совпавшие строки объединяются с первым появлением.

Если ФАЙЛ не задан, читает стандартный ввод (с завершением через Ctrl + D).  

позиционные аргументы:      
  files        файлы для обработки      

опциональные аргументы:        
  -h, --help   показать эту справку и выйти        
  
*примеры использования*    
   
> `$ ./cat.py file4.txt`    
> Hello from line1 of file4.txt!    
> Hello from line1 of test4.txt!   
> Hello from line3 of test4.txt!   
> Hello from line4 of test4.txt!    
> Hello from line1 of test4.txt!    
>    
> `$ ./cat.py file4.txt | ./uniq.py`    
> Hello from line1 of test4.txt!   
> Hello from line3 of test4.txt!   
> Hello from line4 of test4.txt!  
> 
> `$ ./uniq.py file1.txt file4.txt`    
> Hello from file1.txt!   
> Hello from line1 of test4.txt!   
> Hello from line3 of test4.txt!   
> Hello from line4 of test4.txt!   

### troubleshooting

**Trouble:**   
-bash: ./script.py: Permission denied   

**Shooting:**   
`$ chmod +x script.py`   

**Trouble:**   
-bash: env: python\r: No such file or directory  

**Shooting:**   
`$ vim script.py`

Vim Command mode:     

`:set ff=unix`  

`:wq`

