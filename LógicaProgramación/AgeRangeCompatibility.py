"""
Everybody knows the classic "half your age plus seven" dating rule that a lot of people follow (including myself). It's the 'recommended' age range in which to date someone.
Task

Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.

This equation doesn't work when the age <= 14, so if the age <= 14, use this equation instead:

min = age - 0.10 * age
max = age + 0.10 * age
You should floor all your answers so that an integer is given instead of a float (which doesn't represent age). Return your answer in the form "[min]-[max]"

"""

import math

def dating_range(age):
    
    if age > 14:
        
        minAge = age / 2 + 7
        
        maxAge = 2 * (age - 7)
        
        result = str(math.floor(minAge)) + "-" + str(math.floor(maxAge))
        
    else:
        
        minAge = age - 0.10 * age
        
        maxAge = age + 0.10 * age
        
        result = str(math.floor(minAge)) + "-" + str(math.floor(maxAge))
    
    return result

print(dating_range(17))