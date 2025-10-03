# Question 5  is a program which loops allowing the user to use the program over and over again until a password is set
Bad_Passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    new_password = input("Enter a new password. It must contain between 8 to 12 characters: ")
    check_password = input("Re-Enter the password: ")

    new_password = str(new_password)
    check_password = str(check_password)

    if len(new_password) < 8 or len(new_password) > 12:
        print("The password is not in the specified format. Please try again")
        continue

    elif new_password in Bad_Passwords:
        print("The password you entered is not strong enough, please re-try and choose a stronger password")
        continue

    elif new_password == check_password:
        print("***Password set***")
        break
    else:
        print("Passwords entered do not match, please re-enter passwords and try again")
        continue