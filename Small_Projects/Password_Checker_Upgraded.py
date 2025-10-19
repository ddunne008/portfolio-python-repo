# Question 3 checks if the password entered is between 8 and 12 characters
new_password = input("Enter a new password. It must contain between 8 to 12 characters: ")
check_password = input("Re-Enter the password: ")

new_password = str(new_password)
check_password = str(check_password)

if len(new_password) < 8 or len(new_password) > 12:
    print("The password is not in the specified format. Please try again")

    if new_password == check_password and len(new_password) < 8 and len(new_password) > 12 == False:
        print("***Password set***")
    else:
        print("Passwords entered do not match, please re-enter passwords and try again")