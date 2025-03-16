def linear_search(list, target):
    """
    The linear search algorithm is a sequential algorithm that compares each item in the list until the target if found or the list ends

    Returns the index position of the target if found, else returns None

    """

    for i in range(0, len(list)):  # Loop through the list
        if list[i] == target:  # Check if the current item is the target
            return i  # Return the index position of the target
    return None  # Return None if the target is not found


def verify(index):
    if index is not None:  # !== null javascript equivalent
        print(f"Target found at index: {index}")
    else:
        print("Target not found in the list")


# list declaration
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# we pass the list and the target to the linear_search function
result = linear_search(numbers, 6)
# Verify the result
verify(result)
