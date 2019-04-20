#  Write a Python program to construct the following pattern, using a nested loop number.
# Expected Output:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


i = 1                             # intialize i
number = input("Enter a number")  # take input number
while i < number:                 # iterate the loop untill the condition will not false
    j = 1                         # intialize j
    while j <= i:                 # check the condition the inner loop will work till j<=i
        print i,                  # print the value of i this , (comma) will use to make the value in one line
        j +=1                     # increment of j
    print                         # print is use as next line statement 
    i +=1