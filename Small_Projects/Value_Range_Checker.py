#This program will ask the user to input a number, if the number is between the range of 0 and 100
#it will return the value TRUE
#if it is not, it will return the value FALSE.

#This function will return a TRUE or FALSE value depending if its within the range 0 to 100
def validate(number):
    return 0 <= number <= 100

print(validate(int(input("Enter a number: "))))