# Question 5 is a program which calculates the maximum, minimum and mean temperatures from the Command line argument entered
import sys

temperatures = sys.argv[1:]
if sys.argv == "":
    print("There are no arguments given")

def max_calc():
    max_temp = max(temperatures)
    return max_temp

def min_calc():
    min_temp = min(temperatures)
    return min_temp

def mean_calc():
    mean_temp = sum(temperatures) / len(temperatures)
    return mean_temp

max_temp = max_calc()
min_temp = min_calc()
mean_temp = mean_calc()

print("The Minimum temperature is: ", min_temp , "C")
print("The Maximum temperature is: ", max_temp , "C")
print("The Mean Temperature is: ", mean_temp , "C")