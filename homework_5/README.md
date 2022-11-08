# Python_BI_2022
**Python_BI_2022** - это публичный репозиторий для работы с домашними заданиями по Python в Институте биоинформатики.
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


