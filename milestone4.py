import random


###### ---- Define Hangman class-------------------------------------------
class Hangman():


    ###### ---- This is the constructor function // accessed using self.
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.word_list =  word_list
        self.word_guessed = ['_'for x in self.word]
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    ###### ---- Ask for input function
    
    def ask_for_input(self):

        while True:
            guess = input('guess a letter:') 
            if not guess.isalpha() and len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character')
            
            elif guess in self.list_of_guesses:
                print('you already tried that letter!')
            else:
                Hangman.check_guess(self,guess)
                

    ###### ---- Check guess function
    
    def check_guess(self,guess):

        """this function takes the guess and checks whether it is in the word """
        guess = guess.lower()

        
        if guess in self.word:
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    
                    self.word_guessed[i] = self.word[i] 
            

            print('Good guess! {} is in the word and the guessed word is {}'.format(guess, self.word_guessed))
            self.num_letters  -= 1
        else:
            self.num_lives -= 1
            
            print('Sorry, {} is not in the word. Try again'.format(guess))
            print("You have {} lives left.".format(self.num_lives))
            
        self.list_of_guesses.append(guess) 
        print(self.list_of_guesses)    

###### ---- End of Hangman class-------------------------------------------




###### ---- play game function-------------------------------------------
def play_game():
    word_list = ['banana', 'apple', 'pear', 'mango', 'coconut']

    game = Hangman(  word_list, num_lives = 5 )
    
    
    while True:
        if int(game.num_lives) == 0:
            
            print('you lost, the word was {}!'.format(game.word))
            
            break
        elif game.num_letters > 0 :
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print('congratulations you ve won, the word was {}!'.format(game.word))
        else:
            pass
        
play_game()
