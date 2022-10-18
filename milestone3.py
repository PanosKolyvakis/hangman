import random


###### ---- Define Hangman class
class Hangman:

    ###### ---- Below are the initialised class variables // accessed using Hangman.
    word_list = ['banana']
    word = random.choice(word_list)
    word_guessed = [print('_') for x in word]
    num_letters = len(word)
    num_lives = 5
    list_of_guesses = []

    ###### ---- This is the constructor function // accessed using self.
    def __init__(self, word, num_lives):
        self.word = word
        self.num_lives = num_lives

    ###### ---- Ask for input function
    @classmethod
    def ask_for_input(cls):

        while True:
            guess = input('guess a letter:') 
            if not guess.isalpha() and len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character')
            
            elif guess in Hangman.list_of_guesses:
                print('you already tried that letter!')
            else:
                Hangman.check_guess(guess)
                

    ###### ---- Check guess function
    @classmethod
    def check_guess(self,guess):

        """this function takes the guess and checks whether it is in the word """
        guess = guess.lower()

        
        if guess in self.word:
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    
                    Hangman.word_guessed[i] = self.word[i] 
            

            print('Good guess! {} is in the word and the guessed word is {}'.format(guess, Hangman.word_guessed))
            Hangman.num_letters  -= 1
        else:
            self.num_lives -= 1
            
            print('Sorry, {} is not in the word. Try again'.format(guess))
            print("You have {} lives left.".format(self.num_lives))
            
        Hangman.list_of_guesses.append(guess) 
        print(Hangman.list_of_guesses)    




Hangman.ask_for_input()