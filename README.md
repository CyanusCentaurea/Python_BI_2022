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


