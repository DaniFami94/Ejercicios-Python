def binary_search(list, target):
    """
    Binary search works by breaking the array or list down into smaller sets until we find the value we`re looking for.
    """
    first = 0  # First element of the list
    last = len(list) - 1  # Last element of the list, the -1 is because the index starts at 0, for example, a list with 10 elements will have the last element at index 9 not 10

    while first <= last: # Loop until the first element is less than or equal to the last element
        
        midpoint = (first + last) // 2  # Find the middle element of the list, the // operator is used to perform integer division for example first:0 + last:7  = 7 // 2 = 3 it does not return a decimal value

        if list[midpoint] == target:
        
            return midpoint  # If the middle element is the target value, return the index of the middle element, this is the best case scenario for the algorithm
    
        elif list[midpoint] < target: # If the middle element is less than the target value, we need to search the right side of the list
        
            first = midpoint + 1 # The value of midpoint increases by 1 each iteration  until the target value is found or the list ends
    
        else:
        
            last = midpoint - 1 # The value of midpoint decreases by 1 each iteration  until the target value is found or the list ends
    
    return None  # Return None if the target is not found


def verify(index):
    if index is not None:  # !== null javascript equivalent
        print(f"Target found at index: {index}")
    else:
        print("Target not found in the list")


# list declaration
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # in this case the list is sorted, if the list is not sorted the binary search algorithm will not work
# we pass the list and the target to the binary_search function
result = binary_search(numbers, 6)
# Verify the result
verify(result)
