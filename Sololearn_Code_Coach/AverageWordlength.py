import math
from string import ascii_letters as alphabet

def averageWordLength(sentence):
    allLetters = [letter for letter in sentence if letter != " " and letter in alphabet]
    allWords = sentence.split(" ")
    
    average = len(allLetters) / len(allWords)
    return math.ceil(average)
    
while True:
    sentence = input()
    print(averageWordLength(sentence))   