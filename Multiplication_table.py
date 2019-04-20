#Write a Python program to create the multiplication table (from 1 to 10) of a number.

i=1                                                        # initialize i
number=input("Enter a number whose table you want to know")# input a number
temp = 10                                                  # temp variable store 10 
while(i<=temp):                                            # loop will iterate till condition not false
	table = number*i                                       # table store the value of the multiplication of number and i 
	i=i+1                                                  # increment of i
	print table                                            # print the value of varible table
    
