 # Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case)

string = raw_input("Enter a string")  #Take input
for i in range(0, len(string)):       #iterate the loop till the range of the length of string
 	temp = ord(string[i])             #ord() function returns the number representing the unicode code of a specified character. Example ord('A') = 65
 	if temp>65 and temp<=122:         #check the conditon
 		temp = ord(string[i])           
 		temp = temp + 32              #add the value of temp in temp+32 because thier is diffence 32 in the ascii value od A and a letter
 		c = chr(temp)                 #The chrt() method returns a character (a string) from an integer (represents unicode code point of the character) , "Example chr(97) = a"
 		print c                       #print the value c

