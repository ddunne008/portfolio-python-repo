#This program greets the user and prompts the user to enter its name
#It will firstly, change the first letter of the name into an uppcase even if it is already using indexing
#Secondly the program will change the next letter along and the rest of the characters to lowercase


def checkuppercase(name):
    name = name[0].upper() + name[1:].lower() #This code will change the first letter in the name to a uppercase and the rest in lowercase
    return name

#This code greets the user and asks for their name, it will then use the checkuppercase function and print out its name in the correct format
name = input("Greetings, What is your name?: ")
name = checkuppercase(name)
print("Hello there,", name, "nice to meet you")

