#create bigrams
#perform one letter into one or more bigrams 
#do vigenere encryption
#transfer bigram mapping into a key
#decode and obtain the original message

import random
import string

def generate_bigrams():
    letters = string
    letters = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
    bigrams = []
    for a in letters:
        for b in letters:
            if a != b:
                bigrams.append(a+b)
    return bigrams