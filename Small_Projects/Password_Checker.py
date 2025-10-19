# Question 2 is a program which checks the password entered is the same and will let the user know
new_password = input("Enter a new password: ")
check_password = input("Re-enter the password: ")

new_password = str(new_password)
check_password = str(check_password)

if new_password == check_password:
    print("***Password set***")
else:
    print("Passwords entered do not match, please re-enter passwords and try again!")