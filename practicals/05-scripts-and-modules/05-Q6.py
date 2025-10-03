# Question 6 is a program which creates a back-up of a file entered using a command line argument
import sys
import shutil # This is a function imported so it can make a copy of a file


file_name = sys.argv[1]

backup_file = file_name + "-copy1"

shutil.copy(file_name, backup_file)

print("The copy has been successful!")