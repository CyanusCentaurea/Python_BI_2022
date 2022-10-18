# Python_BI_2022
**Python_BI_2022** - это публичный репозиторий для работы с домашними заданиями по Python в Институте биоинформатики.
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


