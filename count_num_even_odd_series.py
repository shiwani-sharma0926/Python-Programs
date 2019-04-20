# Write a Python program to count the number of even and odd numbers from a series of numbers.

# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output : 
# Number of even numbers : 5
# Number of odd numbers : 4

numbers = (1,2,3,4,5,6,7,8,9)
add_odd = 0
add_even = 0
i=0
while(i<=numbers):
	if i%2==0:
		add_odd = add_odd + 1
	else:
		add_even = add_even + 1
print "Total odd number" ,  add_odd
print "Total even number" , add_even