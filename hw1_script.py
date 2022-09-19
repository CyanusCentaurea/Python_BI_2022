complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'U': 'A'}


def complement(seq):
    complement_seq = ''
    for nucl in seq:
        if nucl.islower():
            complement_seq += complement_dict[nucl.upper()].lower()
        else:
            complement_seq += complement_dict[nucl]
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
            print(transcribe(sequence))
        elif command in ['reverse', 'r']:
            print(reverse(sequence))
        elif command in ['reverse complement', 'rc']:
            sequence = reverse(sequence)
            print(complement(sequence))

