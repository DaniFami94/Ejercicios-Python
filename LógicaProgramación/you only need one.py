"""
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

a can contain numbers or strings. x can be either.

Return true if the array contains the value, false if not.
"""

arrayOfElements = [1,2,3]
value = 2

def check(arrayOfElements,value):

    for element in arrayOfElements:
        if element == value:
            return True
    
    return False
        
        
print(check(arrayOfElements,value))