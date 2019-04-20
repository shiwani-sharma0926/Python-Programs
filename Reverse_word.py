# Python program that accepts a word from the user and reverse it.

# word = ["s","h","i","v","a","n","i"]
word = raw_input("Enter a word")
length = len(word)
empty_list = []
i=0
while(i<length):
	empty_list.append(word[length-1-i])
	i=i+1
