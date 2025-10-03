# Question 1 is a function which converts a number to binary
def convert_to_binary(n):
    if n <= 0:
        print("The number must be a positive number")
    else:
        return bin(n)[2:] # This code is calling the bin() function which calculates the binary and filters out the BI letters at the start, displaying the biary value only

print(convert_to_binary(192))