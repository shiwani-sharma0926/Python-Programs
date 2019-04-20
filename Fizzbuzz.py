# Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

i=0                            # initialize i
num=50                         # assign value in the varialble in num
while(i<=num):                 # iterate the loop untill the condition will false
	if i%5==0 and i%5==0:      # check the condition that i is divisible by 3 and 5  
		print "FizzBuzz"       # print FizzBuzz
		i=i+1                  # increment the value of i
	elif i%3==0:               # if the first condition of false then elif part is execute
		print "Fizz"
		i=i+1
	elif i%5==0:               
		print "Buzz"
		i=i+1
	else:                      # if condition will false then else execute
		print i                # print the value i
		i=i+1                  # increment i




		
