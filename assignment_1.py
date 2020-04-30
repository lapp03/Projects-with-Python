"""
Name: Alfredo Pena
Class: CS 241
Professor: Bro. Macbeth

This program selects a random number and prompts the user for a guess.
As the user inputs his or her guesses, the program will give hints until
the user guesses correctly: fun, simple, and entertaining!
"""

############################ MAIN CODE ##################################

#Downloads the randint function so it can select a random numer for the user.
import random
from random import randint             

#Displays an welcome message and prompts user for a seed.
print("Welcome to the number guessing game!")
my_seed = input("Enter random seed: ")

#Sets seed generator.
random.seed(my_seed)

start = "begin"
print()

while start != "stop":
    rand_num = randint(1,100)        #Selects a random number between 1 and 100.
    counter = 0                                                
    
    while counter != "stop":         #Loops through the whole game until the user doesn't want to play.
        guess = int(input("Please enter a guess: "))  #Asks the user to enter a guess. 
        counter += 1                 #Will add a number to the counter each time the user inputs a guess. 
        
        if guess > rand_num:         #If the user's input is higher than the answer, it will display "Lower".
            print("Lower")
            print()
            
        elif guess < rand_num:       #If the user's input is lower than the answer, it will display "Higher".
            print("Higher")
            print()
            
        else:                        #Will congratulate the user when the user's input matches than the answer. 
            print("Congratulations. You guessed it!")
            print("It took you {} guesses.".format(counter)) #Displays the number of total guesses in the match.
            print()
            
            repeat = input("Would you like to play again (yes/no)? ") #Ask the user if he/she wants to play again.
            if repeat == "yes":      #It will reset the counter and select another random number. 
                counter = 0         
                rand_num = randint(1,100)
                
            else:                    #It will exist the outer "while" loop, thus ending the game.   
                counter = "stop"
                start = "stop"
                
print("Thank you. Goodbye.")         #It displays a goodbye message. 
        
        


        

