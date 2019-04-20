# Python program to guess a number between 1 to 9.

# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.


import random                             #To access random module we import the random import we need in the program to choose the random number.
guess = random.randint(1,9)               #guess is a variable in which the randint function is assign, randint is used when we need random integer.
i=0                                       #Initialization of i
while i<9:                                #Loop will iterate untill the condition will not false check condition i<9 or not
	number = input("Enter any number 1 to 9") #Input number in beetween 0 to 9
	if(number!= guess):                   #check the condition number is not equal to guess
		i=i+1                             #increment the value of i
	else:                                 #if condition will not true then execute the else part
		print "well guessed"              #print statement
		break                             #break is used to skip the rest of the instructions 
		                                  #in the loop and begin the next iteration
