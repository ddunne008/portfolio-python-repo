# Question 7 is a program which calculates the maximum, minimum and mean temperature from a list of temperatures
temperatures = [20, 21, 14, 19, 21, 10]

def max_calc():
    max_temp = max(temperatures)
    return max_temp

def min_calc():
    min_temp = min(temperatures)
    return min_temp

def mean_calc():
    mean_temp = sum(temperatures) / len(temperatures)
    return mean_temp

max_temp = max_calc() #This calls the max_calc function
min_temp = min_calc() #This calls the min_calc function
mean_temp = mean_calc() #This calls the mean_temp function

# This code then displays the temperatures on the users screen
print("The Minimum Temperature is: ", min_temp , "C")
print("The Maximum temperature is: ", max_temp , "C")
print("The Mean Temperature is: ", mean_temp , "C")
