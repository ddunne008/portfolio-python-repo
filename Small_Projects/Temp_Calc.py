# Question 8 calculates the minimum, maximum and mean temperatures. It also filters spaces between nultiple temperatures

# WIP, It only currently prints the Maximum temperature will need further improvements
temperatures = input("Enter the temperatures: ")
temperatures.replace('.', '', 1)


def max_calc(a):
    max_temp = max(a)
    return max_temp

def min_calc(b):
    min_temp = min(b)
    return min_temp

def mean_calc(c):
    c = int(c)
    mean_temp = sum(c) / len(c)
    return mean_temp


print("The Minimum Temperature is: ", min_calc(temperatures) , "C")
print("The Maximum temperature is: ", max_calc(temperatures) , "C")
print("The Mean Temperature is: ", mean_calc(temperatures) , "C")