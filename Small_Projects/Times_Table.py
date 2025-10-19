# Question 6 is a program which calculates the times tables of a given number entered by the user
times_table = int(input("Enter the times table number: "))


if times_table <= 0 or times_table <= 12:
    for a in range(13):
        print(f"{a} * {times_table} = {a * times_table}")
else:
    print("Please enter a number between 0 or 12")