# This is a Python program which converts miles to kilometers when the user enteres a value. It quits the program if the
# user entered a negative number like -4

miles = input("Enter the miles value: ")
miles = int(miles) # Integer data type was used instead of float, so it can be shortened
if miles < 0:
    print("The number should not be a negative number")
    quit()

kilometers = miles * 1.609 # This calculates meters to kilometers.

print(f"{miles} is equivalent to {kilometers} kilometers")