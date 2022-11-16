import re
import seaborn as sns
import matplotlib.pyplot as plt


# references.txt parsing to find all ftp links. Redirecting output to ftps.txt
# Version that only searches for links ending with a file extension (e.g. ftp.sra.ebi.ac.uk/vol1/fastq/ERR106/001/ERR1063831/ERR1063831_1.fastq.gz)
with open('references.txt') as references:
        line = references.readline().strip()
        while line:
            with open('ftps.txt', 'a') as ftps:
                for ftp in re.findall(r'ftp.sra.ebi.ac.uk\/[^;\s]+\.\w+', line):
                    print(ftp, file=ftps)
            line = references.readline().strip()


# references.txt parsing to find all ftp links. Redirecting output to ftps.txt
# Version that only searches for everything looks like ftp-link (ftp.sra.ebi.ac.uk/vol1/err/ERR212/ERR212133 too)
with open('references.txt') as references:
    line = references.readline().strip()
    while line:
        with open('ftps.txt', 'a') as ftps:
            for ftp in re.findall(r'ftp.sra.ebi.ac.uk\/[^;\s]+', line):
                print(ftp, file=ftps)
        line = references.readline().strip()


#  2430 A.D..txt parsing to find and print all numbers
with open('2430 A.D.txt') as story:
    while True:
        line = story.readline()
        for number in re.findall(r'\d+[.]*\d+', line):
            print(number)
        if not line.endswith('\n'):
            break


#  2430 A.D..txt parsing to find and print all words contain 'a' letter ignoring register
with open('2430 A.D.txt') as story:
    while True:
        line = story.readline()
        for number in re.findall(r'\b\w*[Aa]\w*\b', line):
            print(number)
        if not line.endswith('\n'):
            break


#  2430 A.D..txt parsing to find and print all exclamatory sentences
with open('2430 A.D.txt') as story:
    while True:
        line = story.readline()
        for exclamatory in re.findall(r'[A-Z][^\.!\?]+\!', line):
            print(exclamatory)
        if not line.endswith('\n'):
            break


#  2430 A.D..txt parsing to find all words (words with apostrophes counted as one word, apostrophe counted as a letter,
#  e.g. "we'll" counted as one word of five letters). A dictionary was used to find all unique words ignoring register.
unique_words = {}
with open('2430 A.D.txt') as story:
    while True:
        line = story.readline()
        for word in re.findall(r"\b[a-zA-Z']+\b", line):
            if not unique_words.get(len(word)):
                unique_words[len(word)] = {word.lower()}
            else:
                unique_words[len(word)].add(word.lower())
        if not line.endswith('\n'):
            break
unique_words_count = {k: len(v) for k, v in unique_words.items()}
unique_words_count_plot = sns.barplot(x=list(unique_words_count.keys()),
                                      y=list(unique_words_count.values()))
unique_words_count_plot.set_title('Unique words (without numbers) lengths count\nin the story "2430 A.D."')
unique_words_count_plot.set_xlabel('Unique words lengths')
unique_words_count_plot.set_ylabel('Count')
plt.show()

unique_words_proportion = {k: v / sum(unique_words_count.values()) for k, v in unique_words_count.items()}
unique_words_proportion_plot = sns.barplot(x=list(unique_words_proportion.keys()),
                                           y=list(unique_words_proportion.values()),
                                           color='orange')
unique_words_proportion_plot.set_title('Proportion of unique words of a given length of the total number\nof unique words in the story "2430 A.D."')
unique_words_proportion_plot.set_xlabel('Unique words lengths')
unique_words_proportion_plot.set_ylabel('Proportion')
plt.show()

unique_words_percent = {k: v * 100 / sum(unique_words_count.values()) for k, v in unique_words_count.items()}
unique_words_percent_plot = sns.barplot(x=list(unique_words_percent.keys()),
                                        y=list(unique_words_percent.values()),
                                        color='green')
unique_words_percent_plot.set_title('Proportion (in percent) of unique words of a given length of\nthe total numberof unique words in the story "2430 A.D."')
unique_words_percent_plot.set_xlabel('Unique words lengths')
unique_words_percent_plot.set_ylabel('Proportion (in percent)')
plt.show()


# A russian text translation into a brick language (using 'c' with vowel after vowel)
def brick_language(text):
    """
    Takes a russian text as an argument and returns translation into a secret brick language.
    """
    text = re.sub(r'([АОУЫЭЕИЮЯаоуыэеиюя])', r'\1' + 'c' + r'\1', text)
    return text


# print(brick_language('Шла Саша по шоссе и сосала сушку, а я сяду в кабриолет и поеду куда-нибудь'))
# Чуть не сдала задание с этим тестом, а потом думаю, дай оставлю, может, он и вам понравится :D

def find_n_words_sentences(text, n):
    """
    Function for extracting sentences with a given number of words from the given text.
    The function takes two arguments: a text (string) and a number of words (int) in the sentence.
    Returns a list of tuples, each containing words from the found sentences.
    """
    res = []
    for sentence in re.findall(r'''[A-ZА-Я][\wа-яА-Я ,;:\-"'()]+''', text):
        words = tuple(re.findall(r"[a-zA-Zа-яА-Я]+[\wа-яА-Я'\-]*\s*", sentence))
        if len(words) == n:
            res.append(words)
    return res

