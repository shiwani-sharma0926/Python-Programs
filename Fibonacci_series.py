  # . Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34


i=0                                   #initialize the i
number = 50                           #assign the value 50 in number variable
first_num = 0                         #assigning the value in variable
second_num =1                         #assigning the value in variable
while(i<number):                      #iterate the loop it will iterate till the condition will not false
	result = first_num + second_num   #storing the addition of value in variable name result
	print result                      #print the result
	i=i+1                             #increment of i
	first_num = second_num            #the second_num will store in first_num
	second_num = result               #result will store in second_num
