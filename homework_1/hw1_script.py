"""Необходимо реализовать программу, которая в бесконечном цикле считывает команды от
пользователя. После команды программа должна запрашивать у пользователя
последовательность нуклеиновой кислоты и распечатывать результат.
Список команд:
exit — завершение исполнения программы
transcribe — напечатать транскрибированную последовательность
reverse — напечатать перевёрнутую последовательность
complement — напечатать комплементарную последовательность
reverse complement — напечатать обратную комплементарную последовательность
+ любые дополнительные команды на ваш страх и риск (опционально)
Требования:
Программа должна сохранять регистр символов (напр. complement AtGc это TaCg)
Программа должна работать только с последовательностями нуклеиновых кислот. К примеру, последовательность AUTGC не может
существовать, так как содержит T и U, такие случаи нужно обрабатывать и сообщать об этом пользователю (см. пример).
Запрещается использование сторонних модулей
"""

complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'U': 'A', 'a': 't', 't': 'a', 'g': 'c', 'c': 'g', 'u': 'a'}


def complement(seq):
    complement_seq = ''.join([complement_dict[nucl] for nucl in seq])
    return complement_seq


def transcribe(seq):
    transcribed_seq = seq.replace('T', 'U')
    transcribed_seq = transcribed_seq.replace('t', 'u')
    return transcribed_seq


def reverse(seq):
    reversed_seq = seq[::-1]
    return reversed_seq


print('Hello!')
while True:
    command = input('Enter command (Use "exit" or "e", "transcribe" or "t",'
                    '"reverse" or "r", "complement" or "c", "reverse complement" or "rc"): ')
    while command not in ['exit', 'e', 'transcribe', 't', 'reverse', 'r',
                          'complement', 'c', 'reverse complement', 'rc']:
        print('Invalid command. Please, try again.')
        command = input('Enter command: ')
    if command in ['exit', 'e']:
        print('Good luck!')
        break
    else:
        sequence = input('Enter sequence: ')
        while 'T' in sequence.upper() and 'U' in sequence.upper() or not all([i in 'ATUGCatugc' for i in sequence]):
            print('Invalid sequence. Please, try again.')
            sequence = input('Enter sequence: ')
        if command in ['complement', 'c']:
            print(complement(sequence))
        elif command in ['transcribe', 't']:
            if 'U' in sequence or 'u' in sequence:
                print('It seems to be an RNA sequence. Please, try again with DNA.')
            else:
                print(transcribe(sequence))
        elif command in ['reverse', 'r']:
            print(reverse(sequence))
        elif command in ['reverse complement', 'rc']:
            sequence = reverse(sequence)
            print(complement(sequence))


