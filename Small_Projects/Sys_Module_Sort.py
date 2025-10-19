# Question 3 is a program which sorts different command line arguments and returns the shortest one
import sys

output = sys.argv[1:]
sys.argv.sort()


print(output)