#Python program to convert month name to a number of days. 


print("Listof months: January, February, March, April, May, June, July, August, September, October, November, December ")
month_name = raw_input("Input the month name:")
if (month_name == "january" or month_name == "March" or month_name == "May"or month_name == "July" or month_name == "August"or month_name =="October"or month_name == "December"):
	print("Number of days: 31 day")
elif(month_name =="April"or month_name == "June" or month_name == "September"or month_name =="November"):
	print("Number of days: 30days")
elif month_name == "February":
	print("Number of days: 28 / 29days")
else:
	print("Wrong month name")