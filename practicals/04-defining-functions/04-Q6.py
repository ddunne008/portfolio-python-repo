# Question 6 is a program which calculates Celcius temperature to Fahrenheit
def celcius_fahrenheit(temp):
    temp = float(temp)
    F = temp * 1.8 + 32
    return F



a = input("Enter the temperature in Celcius: ")
if "c" not in a:
    print("The temperature should have a C after the number")
else:
    a = a[:2] #This code filters the input by getting rid of the C so the calculation can work with the number values
    a = float(a)
    temp = float(celcius_fahrenheit(a)) #This code ensures the answer is a float
    print(a,"C", "Translates to the temperature in fahrenheit as:", temp, "F")