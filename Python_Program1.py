# Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).


for i in range(1500,2700):  #Iterate the loop in the range of 1500 to 2700, initially the value of i is 1500.
    if i%5==0 and i%7==0:   #Check the condition that i is divisible by 7 as well as i is a multiple of 5 
        print i             #print the value which is multiple of 5 and divisible by 7

