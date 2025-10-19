# Question 4 is a program which encrypts a message by removing space keys and flipping the phrase in reverse
message = input("Enter a message to encrypt: ")
message = list(message) # This converts the message varible into a list
message.append(message) # This assigns the message into the list


while " " in message:
    message.remove(" ") # This code removes any spaces if it detects any spaces to start with

message.reverse() # This code then reverses the phrase
print("Encrypted Message: ", message)
