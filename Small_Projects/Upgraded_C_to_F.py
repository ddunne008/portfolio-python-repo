#This program calculates Celcius to Fahrenheit and vice versa.

#This function calculates the Fahrenheit temperature to Celcius
def convert_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius

#This function calculates the Celcius temperature to Fahrenheit
def convert_fahrenheit(celcius):
    fahrenheit = celcius * (9/5) + 32
    return fahrenheit



#This code is the first output the user will see. It will ask what covert formulea to choose
#The user must enter option 1 or 2 otherwise it will print an error
print("***Celcius to Fahrenheit convert program***")

print("Option 1 - Celcius to Fahrenheit")
print("Option 2 - Fahrenheit to Celcius")

option = int(input("Which option would you like to open: "))

if option == 1:
    #If the user chooses option 1 to covert Celcius to Fahrenheit, this code will calculate the answer and display it to the user
    C = int(input("Enter the Celcius Temperature: "))
    F = convert_fahrenheit(C)
    print("The Celcius temperature in Fahrenheit is: ", F)

elif option == 2:
    #If the user chooses option 2 to convert Fahrenheit to Celcius, this code will calculate the answer and display it to the user
    F = int(input("Enter the Fahrenheit Temperature: "))
    C = convert_celcius(F)
    print("The Fahrenheit temperature in Celcius is: ", C)

else:
    print("Please select either option 1 or 2")