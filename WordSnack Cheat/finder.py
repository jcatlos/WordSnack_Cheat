import re
from itertools import *

files = ['', '1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt', '8.txt', '9.txt', '10.txt']

lettersInput = input("Insert space-separated list of letters: \n")
wordLength = input("Insert the length of word or 'exit' to end: \n")

while(wordLength != 'exit'):
    letters = lettersInput.split()

    lettersString = ''
    for letter in letters:
        lettersString += letter

    regex = '[' + lettersString + ']{' + wordLength + '}'
    #print(regex)

    with open(files[int(wordLength)], 'r') as f:
        words = f.read()
        matchedWords = re.findall(regex, words, re.M|re.I)

    #print(matchedWords)

    finalWords = []
    possibleWords = []
    possibleWordsList = list(permutations(lettersString, int(wordLength)))

    for i in possibleWordsList:
        word = ''
        for j in i:
            word += j
        possibleWords.append(word)

    for word in possibleWords:
        if word in matchedWords:
            finalWords.append(word)

    print(finalWords)
    wordLength = input("Insert the length of word or 'exit' to end: \n")