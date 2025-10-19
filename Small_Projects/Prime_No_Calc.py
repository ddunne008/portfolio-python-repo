# Question 3 calculates if the entered number by the user if a prime number
n = input("Enter a number: ")

for i in range(2, n):
    if n % i == 0: # This code checks to see if it can involve 2 or itself without leaving a decimal
        print("The number isnt a prime number")
        break
else:
    print("The number is prime")