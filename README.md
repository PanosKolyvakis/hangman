# hangman milestone4.py

- Final Game for Hangman that works without errors. Had some issues tried to define attributes as class variables which did not allow me to use then in the play_game function. fixed by initialising all in the constructor. also added a replay () function that asks the user if they want to replay the game.  Another issue I had was getting the code in the while loop of the play game function to run - but this was becasue i accidentally deleted a break statement in a previous function and the program was not exiting the a previous loop. 

Overall very fun and interesting exercise. Became more used to OOP which i find confusing at times.



# hangman milestone3.py

-had some issues with OOP but ended up going around them by inputing class variables which the different methods of the class 
are calling upon to keep the game working. the code includes additional statements such as printing the list of previous guesses 
to ensure that the code is running smoothly.

-defining the vars outside the class also possible - and perhaps easier to edit.

-the list comprehension [print('_') for x in word] prints the lines vertically for some reason, forgot to fix will do later.
