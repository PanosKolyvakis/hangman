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
            guess = input( 'guess a letter:') 
            if (guess.isalpha() == False) or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character')
                break
            elif guess in self.list_of_guesses:
                print('you already tried that letter!')
            else:
                Hangman.check_guess(self,guess)
                break
                

    ###### ---- Check guess function
    
    def check_guess(self,guess):

        """this function takes the guess and checks whether it is in the word """
        guess = guess.lower()

        
        if guess in self.word:
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    
                    self.word_guessed[i] = self.word[i] 
                    self.num_letters  -= 1

            print('\n' 'Good guess! {} is in the word and the guessed word is {}'.format(guess, self.word_guessed))
            
            print( '\n' 'The number of guesses to win: {}'.format(self.num_letters))
        else:
            self.num_lives -= 1
            
            print('\n''Sorry, {} is not in the word. Try again'.format(guess))
            print('\n' "You have {} lives left.".format(self.num_lives))
            
        self.list_of_guesses.append(guess) 
        
        print('\n' 'The list of guesses so far is {}'.format(self.list_of_guesses))    
        

    def play_again(self):

        retry = input('\n' 'do you want to play again?').lower()
        if retry == "y" or retry == "yes":
            play_game()
        else:
            
            exit()

###### ---- End of Hangman class-------------------------------------------




###### ---- play game function-------------------------------------------
def play_game():
    word_list = ['banana', 'apple', 'pear', 'mango', 'coconut']

    game = Hangman(   word_list , 5  )
    
    
    while True:

        if game.num_lives == 0:
            
            print('\n' + 'you lost, the word was {}!'.format(game.word))
            game.play_again()
            break
        elif game.num_letters > 0 :
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print('\n' + 'congratulations you ve won, the word was {}!'.format(game.word))
            break
        else:
            pass
        
play_game()


