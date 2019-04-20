# Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
# Expected Output : 
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

                                               
temp_value = input("Enter temperature value:")                                    #input the temperature
temp_type = raw_input("Enter the type of temperature (Celsius/Faherenheit): C/F") #type of the temperature Celcius or Faherenheit 
if temp_type == "C":                                          #check the condition if temp_type is equal to C then find Fehrenhiet
    fehrenheit = ((9*(temp_value)/5)+32)                      #formula for finding fehrenheit 
    print fehrenheit , "Fahrenheit"           
else: 
    celsius = ((5*(temp_value-32))/9)                         #calulate the celsius 
    
    print celsius ,"Celsius"                                
