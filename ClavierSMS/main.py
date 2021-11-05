from typing import Tuple

pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def getFrenchList() -> Tuple:
    with open('liste_francais.txt') as file:
        lines = file.read()
    words_tuple = tuple(word for word in lines.split('\n'))
    return words_tuple


def computeNumbers(numbers: str):
    all_words = getFrenchList()

    words_filtered = []
    for word_filter in all_words:
        if len(word_filter) == len(numbers):
            # print(word_filter)
            words_filtered.append(word_filter)

    words_result = []
    for word in words_filtered:
        word_match = True
        for index, letter in enumerate(word):
            # print("index : ", index, "/ letter :", letter)
            if letter not in pad[numbers[index]]:
                word_match = False
                break
        if word_match:
            words_result.append(word)
    return words_result


print(computeNumbers("2665687"))
print(computeNumbers("72588"))
print(computeNumbers("2662273437"))

# def listLetters(number):
#     list_letters = []
#
#     for i in str(number):
#         if 1 < int(i) < 10:
#             list_letters.append(pad[int(i)])
#
#     return list_letters
