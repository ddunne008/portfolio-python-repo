#This program counts the amount of uppercase and lowercase characters within a word that the user inputs.

#This function overall calculates the amount of lowercase letters within the inputted word.
#It searches through a set of lowercase letters, counts the total from the inputted word and returns it
def no_of_lowercase_letters(word):
    lowercase_letters = set("abcdefghijklmnopqrstuvwxyz")
    lowercase_count = sum(1 for char in word if char in lowercase_letters)
    return lowercase_count

#This function overall calculates the amount of uppercase letters within the inputted word
#Similar to the lowercase letters function, it searches through a set of uppercase letters, counts the total from the inputted word and returns it
def no_of_uppercase_letters(word):
    uppercase_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    uppercase_count = sum(1 for char in word if char in uppercase_letters)
    return uppercase_count

#This part of the program prompts the user to enter a word of their choice, it will then use the above functions to calculate the amount of uppercase and lowercase letters from that word!
word = input("Enter a word of your choice!: ")
print("There are", no_of_lowercase_letters(word), "lower-case letters and", no_of_uppercase_letters(word), "upper-case letters in", (word))