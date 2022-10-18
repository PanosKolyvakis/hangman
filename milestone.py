from secrets import choice
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

print(word.lower)