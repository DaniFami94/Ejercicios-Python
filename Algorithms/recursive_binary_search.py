def recursive_binary_search(list,target):
    """
    Recursive binary search works by breaking the array or list down into smaller sets until we find the value we`re looking for.
    Time complexity of the recursive binary search algorithm is O(log n) because the list is divided in half each time the function is called
    
    """
    if len(list) == 0: # If the list is empty return False
        
        return False
    
    else: 
        
        midpoint = len(list) // 2 # find the middle element of the list and round down the result to the nearest whole number to avoid decimal values 
        
        if list[midpoint] == target: # If the middle element is the target value, return True
            
            return True
        
        else:
            
            if list[midpoint] < target: 
                
                return recursive_binary_search(list[midpoint + 1:],target) # we slice the list from the midpoint + 1 to the end of the list, this makes a new sublist with the right half of the original list
            else:
                return recursive_binary_search(list[:midpoint],target) # the ":midpoint" is used to slice the list from the beginning to the midpoint

# the function len() return the length of the list for example len([1,2,3,4,5,6,7,8]) = 8, starts at 1 not 0
# the range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# recursive call #1:
#   - Original list: [0,1,2,3,4,5,6,7,8]
#   - Midpoint: 4 (len 9 // 2)
#   - Value at midpoint: list[4] = 4
#   - 4 < 8, so we search in the right half
#   - New list: list[midpoint + 1:] = [5,6,7,8]
#   - Target = 8 (not found yet)

# recursive call #2:
#   - Current list: [5,6,7,8]
#   - Midpoint: 2 (len 4 // 2)
#   - Value at midpoint: list[2] = 7
#   - 7 < 8, so we search in the right half
#   - New list: list[midpoint + 1:] = [8]
#   - Target = 8 (not found yet)

# recursive call #3:
#   - Current list: [8]
#   - Midpoint: 0 (len 1 // 2)
#   - Value at midpoint: list[0] = 8
#   - 8 == 8 Target found!
#   - return True

def verify(result):
    
    print(f"Target found: {result}")


# list declaration
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# we pass the list and the target to the recursive_binary_search function
result = recursive_binary_search(numbers, 12)
# Verify the result
verify(result)

result = recursive_binary_search(numbers, 8)
# Verify the result
verify(result)


# 1:40:20