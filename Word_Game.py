"""
This a program designed for enjoyment. It is a game where the player has ten tries to guess a word from a
certian list specified.  
This program will be structed by gathering user name
Setting a timer for user to begin guessing
Importing the randomly selcted words list
setting the number of tries the user has
use a while loop to count the number of tries
print results to user (Win or Lose)
"""

#importing the time module
import time


#welcoming the user
name = raw_input("What is your name? ")

print "Hello, " + name, "Time to play SPELL THAT WORD!"

print " "


#wait for 1 second
time.sleep(1)

print "Start guessing..."
time.sleep(1)

#here we set the secret word
import random
Words_list = ['pineapple', 'apple', 'orange', 'bannana', 'grape', 'lemon', 'cherries', 'plum']

word = random.choice(Words_list)

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:    
        # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print char,    

        else:
    
        # if not found, print a dash
            print "_",     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print("YOU WON!")

    # exit the script
        break              

    print

    # ask the user go guess a Letter
    guess = raw_input("guess a Letter:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")    
 
    # how many turns are left
        print "You have", + turns, 'more guesses' 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose")
