# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


i=0                              # initialization the i
number=input("Enter any number") # take input number
while(i<number):                 # loop will iterate till condition will true i<number
	print '*' * i                # print *
	i = i + 1                    # increment the loop
while(i>0):                      # again iterate the loop for decrement 
	print '*' * i                # print *
	i = i - 1                    # decrement
