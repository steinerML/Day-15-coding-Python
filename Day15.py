# Calculator to convert from Celsius to Farenheit

#User input
temp = float(input("Enter the temperature in Celsius (°C):"))
#Function definition
def convert_celsius(temp):
    return temp * 9/5 + 32 # Returns function to result()

result = convert_celsius(temp) #Calls function
print(result, "F") #Prints result