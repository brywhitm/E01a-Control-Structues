#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 #Prints a string Greetings!
colors = ['red','orange','yellow','green','blue','violet','purple']             #tells what the variable colors is equal to/set to
play_again = ''                     #tells what the variable play_again is equal to/set to
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):       #A while statment that runs until the varialbe play_again is equal to the string n or no
    match_color = random.choice(colors)                 #Sets the variable match_color to a random string from the variable colors
    count = 0                       #sets count to zero
    color = ''                      #creates a variable called color that is equal to an input string
    while (color != match_color):   #A while statment that runs if the color variable is not equal to the variable match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()                   #sets the string input from color to lower case and removes spaces from the end and begining
        count += 1                  #adds one to the variable count
        if (color == match_color):  #if the color input is equal to match_color then do whats next
            print('Correct!')       #print the string Correct
        else:                       #else statment that is only used if the if statment was false
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))      #if the else statment is active then print this string and add the value of count
    print('\nYou guessed it in {0} tries!'.format(count))       #prints a string that tells you how many times it took to get it right
    if (count < best_count):                #if the count is lower then the varialbe best_count then
        print('This was your best guess so far!')       #print the string if the if statment was true
        best_count = count                  #set the count to the varable best count if the if statment was true
    play_again = input("\nWould you like to play again? ").lower().strip()      #The variable play_agian is equal to the input from the string that is then lower cased and removed all spaces before and after
print('Thanks for playing!')            #print the string THANKS FOR PLAYING!