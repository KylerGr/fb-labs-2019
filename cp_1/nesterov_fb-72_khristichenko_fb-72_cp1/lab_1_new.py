import codecs
import math
from collections import Counter

my_text = open("my_text.txt", "r+", encoding='utf-8')
text_one = my_text.read()
my_text.close()


# change in the text with the spaces


def change_text(text):
    change = ""
    for letter in text:
        if letter in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            change = change + letter.lower()
        elif letter in "-!.,;:–»«?()<>":
            change = change + ""
        elif letter in "0123456789":
            change = change + ""
#        elif letter in " ":
#            change = change + ""
        elif letter in "\n":
            change = change + ""
        elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            change = change + ""
        elif letter in "abcdefghijklmnopqrstuvwxyz":
            change = change + ""
        else:
            change = change + letter

    return change


print(change_text(text_one))


# change in the text without the spaces


def change_text_two(text):
    change = ""
    for letter in text:
        if letter in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            change = change + letter.lower()
        elif letter in "-!.,;:–»«?()<>":
            change = change + ""
        elif letter in "0123456789":
            change = change + ""
        elif letter in " ":
            change = change + ""
        elif letter in "\n":
            change = change + ""
        elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            change = change + ""
        elif letter in "abcdefghijklmnopqrstuvwxyz":
            change = change + ""
        else:
            change = change + letter

    return change


# here we have a counter which counts the overall number of symbols in the changed text with the spaces


def letter_count(text_first, count):
    for symbol in text_first:
        if symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ":
            count += 1
        else:
            count = count
    return count


print("Number of characters in the changed text: " + str(letter_count(text_one, 0)))

# here we have a counter which counts the overall number of symbols in the changed text without the spaces


def letter_count_two(text_first, count):
    for symbol in text_first:
        if symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
            count += 1
        else:
            count = count
    return count


# entropy for monogram with the space


def monogram_entropy(text_second):
    amount = Counter("")
    count = 0
    a = text_second
    for symbol in text_second:
        if symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ":
            count += 1
        else:
            count = count
    print("The amount of each symbol in the text is: " + str(Counter(a)))
    array = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    for i in array:
        Counter(a)[i] = 0
    for j in Counter(a):
        Counter(a)[j] += 1
    for k in Counter(a):
        Counter(a)[k] /= count
        print("Here are the sequences: " + str(Counter(a)[k] / count))
    entropy = 0
    for f in Counter(a):
        if Counter(a)[f] > 0:
            entropy -= Counter(a)[f] / count * math.log(Counter(a)[f] / count, 2)
    h = 0
    h = (1 - (entropy / math.log(34, 2)))
    print("Monogram entropy with the spaces is: " + str(entropy))
    print("Below is your H!")
    return h


print("Monograms with spaces")
print(monogram_entropy(change_text(text_one)))


# entropy for monogram without the space


def monogram_entropy_two(text_third):
    amount = Counter("")
    count = 0
    a = text_third
    for symbol in text_third:
        if symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
            count += 1
        else:
            count = count
    print("The amount of each symbol in the text is: " + str(Counter(a)))
    array = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for i in array:
        Counter(a)[i] = 0
    for j in Counter(a):
        Counter(a)[j] += 1
    for k in Counter(a):
        Counter(a)[k] /= count
        print("Here are the sequences: " + str(Counter(a)[k] / count))
    entropy = 0
    for f in Counter(a):
        if Counter(a)[f] > 0:
            entropy -= Counter(a)[f] / count * math.log(Counter(a)[f] / count, 2)
    h = 0
    h = (1 - (entropy / math.log(33, 2)))
    print("Monogram entropy without the spaces is: " + str(entropy))
    print("Below is your H!")
    return h


print(change_text_two(text_one))
print(letter_count_two(text_one, 0))
print("Monogram without spaces")
print(monogram_entropy_two(change_text_two(text_one)))


# here we calculate the amount of bi grams


def bi_gram_amount(text_fourth):
    count = 0
    for letter in text_fourth:
        if letter in "аеёиоуыэюя":
            count += 1
    return count


print("The amount of bi grams is: " + str(bi_gram_amount(change_text(text_one))))


# bi grams with crossing and with spaces


def bi_gram_entropy(text_5):
    amount = Counter("")
    count = 0
    array = [[], []]
    count = 0
    for symbol in text:
        if symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ":
            count += 1
        else:
            count = count
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            array[i][j] = 0
    for i in range(0, len(text) - 1, 1):
        array[text[i:i + 2]] += 1
    for frequency in array:
        array[frequency] /= count // 2
    entropy = 0
    for i in array:
        if array[i] != 0:
            entropy -= array.index(i + j) * math.log(array.index(i + j), 2)
    entropy /= 2
    h = (1 - (entropy / math.log(33, 2)))
    print("Here are the sequences: " + str(dictionary))
    print("Bi gram entropy without the spaces and without crossing is: " + str(entropy))
    print("Below is your H!")
    return h


print(bi_gram_entropy(change_text(text_one)))

# bi grams with crossing and without spaces


def bi_gram_entropy_two(text_6):
    amount = Counter("")
    count = 0
    array = [[], []]
    count = 0
    for symbol in text:
        if symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
            count += 1
        else:
            count = count
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            array[i][j] = 0
    for i in range(0, len(text) - 1, 1):
        array[text[i:i + 2]] += 1
    for frequency in array:
        array[frequency] /= count // 2
    entropy = 0
    for i in array:
        if array[i] != 0:
            entropy -= array.index(i + j) * math.log(array.index(i + j), 2)
    entropy /= 2
    h = (1 - (entropy / math.log(33, 2)))
    print("Here are the sequences: " + str(dictionary))
    print("Bi gram entropy without the spaces and without crossing is: " + str(entropy))
    print("Below is your H!")
    return h


print(bi_gram_entropy_two(change_text_two(text_one)))


# bi grams without crossing and with spaces


def bi_gram_entropy_3(text_7):
    amount = Counter("")
    count = 0
    array = [[], []]
    count = 0
    for symbol in text:
        if symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ":
            count += 1
        else:
            count = count
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            array[i][j] = 0
    for i in range(0, len(text) - 1, 2):
        array[text[i:i + 2]] += 1
    for frequency in array:
        array[frequency] /= count // 2
    entropy = 0
    for i in array:
        if array[i] != 0:
            entropy -= array.index(i + j) * math.log(array.index(i + j), 2)
    entropy /= 2
    h = (1 - (entropy / math.log(33, 2)))
    print("Here are the sequences: " + str(dictionary))
    print("Bi gram entropy without the spaces and without crossing is: " + str(entropy))
    print("Below is your H!")
    return h


print(bi_gram_entropy_3(change_text(text_one)))


# bi grams without crossing and without spaces


def bi_gram_entropy_4(text_8):
    amount = Counter("")
    count = 0
    array = [[], []]
    count = 0
    for symbol in text:
        if symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
            count += 1
        else:
            count = count
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            array[i][j] = 0
    for i in range(0, len(text) - 1, 2):
        array[text[i:i + 2]] += 1
    for frequency in array:
        array[frequency] /= count // 2
    entropy = 0
    for i in array:
        if array[i] != 0:
            entropy -= array.index(i + j) * math.log(array.index(i + j), 2)
    entropy /= 2
    h = (1 - (entropy / math.log(33, 2)))
    print("Here are the sequences: " + str(dictionary))
    print("Bi gram entropy without the spaces and without crossing is: " + str(entropy))
    print("Below is your H!")
    return h


print(bi_gram_entropy_4(change_text_two(text_one)))

entropy1 = 2.75875834011714
entropy2 = 3.3281512757654
entropy3 = 1.62772747153497
entropy4 = 2.30810993761869
entropy5 = 1.36540924206393
entropy6 = 2.11909409803047

h1 = (1 - (entropy1 / math.log(33, 2)))
h2 = (1 - (entropy2 / math.log(34, 2)))
h3 = (1 - (entropy3 / math.log(33, 2)))
h4 = (1 - (entropy4 / math.log(34, 2)))
h5 = (1 - (entropy5 / math.log(33, 2)))
h6 = (1 - (entropy6 / math.log(34, 2)))

print("Your H: " + str(h1))
print("Your H: " + str(h2))
print("Your H: " + str(h3))
print("Your H: " + str(h4))
print("Your H: " + str(h5))
print("Your H: " + str(h6))