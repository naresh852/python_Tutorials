import random
from words import words

def get_valid_word(words):
    word=random.choice(words)
    #for bugs like he roes or he_roes
    while '_' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()
print(get_valid_word(words))