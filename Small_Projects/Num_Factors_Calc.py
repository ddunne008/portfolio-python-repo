# Question 2 is a program which calculates factors of a number using a function which is imported
import sympy # This function allows to calculate factors of a number

def calc_factors(n):
    factors = sympy.factorint(n)
    return factors

print(calc_factors(28)) # This calculates the factors of the value, 28