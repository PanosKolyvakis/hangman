<!-- # Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
 -->
<!-- Milestone 1 -->

<!-- ####### ---Code ------ -->
import random

word_list = ['banana', 'apple', 'pear', 'mango', 'coconut']

print(word_list)

word = random.choice(word_list)
print(word)

guess = input('give me a single letter:')

if len(guess) ==1 and guess.isalpha():
    print('good job')

else:
    print('Oops! that is not a valid input')





<!-- Milestone 2 -->

<!--------Code--->

from curses.ascii import isalpha

import random


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



#--- Comments for both Milestones 1 and 2. Good revision of the basics, loops and functions. Interesting and straight fowrward example



