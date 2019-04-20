# Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4 
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

row = input("Enter row")           # input row
col = input("Enter columm")        # input col
empty = []                         # create a empty array
for i in range(row):               # iterate the loop till the value of row
	empty.append([])               # append the [] in empty 
	for j in range(col):           # iterate the loop till the value of column
		empty[i].append(i*j)       # append the value i*j in empty array by the index
print empty                        # print empty
