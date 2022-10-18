from curses.ascii import isalpha

from pyparsing import Word
from secrets import choice
import random



# word_list = ['banana', 'apple', 'pear', 'mango', 'coconut']

# print(word_list)

# word = random.choice(word_list)
# print(word)
# function for checking if 
def check_guess(guess):

    """this function takes the guess and checks whether it is in the word """
    guess = guess.lower()
    if guess in word:
        print('Good guess! {} is in the word'.format(guess))

    else:
        print('Sorry, {} is not in the word. Try again'.format(guess))

word = 'apple'
def ask_for_input():
    
    while True:
        guess = input('guess a letter:') 
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character')
    check_guess(guess)

ask_for_input()


