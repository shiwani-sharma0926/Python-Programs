# Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement. 
# Expected Output : 0 1 2 4 5 

for i in range(6):     #iterate the loop till the range of 6
	if i==3 or i==6:   #check the condition that the value of i equals to 3 or i equals to 6
		continue       #continue keyword is used to skip current condition and the loop iterate
	print i            #print the value of i
