# Python_BI_2022
**Python_BI_2022** - это публичный репозиторий для работы с домашними заданиями по Python в Институте биоинформатики.

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
> Например, my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4)). my_chain(37) -> (9.75, 9)      