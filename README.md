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