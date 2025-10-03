#This program contains a function which shortens the name which has been typed in using slicing.
#If the name is less than 1 character, it will print the name anyway
def count_letters(name):
    if len(name) > 1:
        return (name[0 : -1])
    else:
        print(name)

#This code prompts the user to enter a name, it will then use the function above to count the letters and shorten the word
name = input("Enter your name: ")
print(count_letters(name))