#Python program to reverse the number


num = input("Enter a number")   #input a number Example:- 1234
rem=0                           #initialize a variable rem(reminder)
rev=0                           #initialize a variable rev(reverse)
while(num>0):                   #iterate the loop till the condition will true 
	rem=num%10                  #num%10 it means 1234%10 => 4, 4 will store in rem
	rev = rev*10 +rem           #rev  = 0*1234+4, so rev will store 4
	num=num//10                 #num = num//10 means 1234//10  => 123
print rev                       #print rev means it will print 4 
                                #again the loop will iterate and check the condition as above and final output will be 4321