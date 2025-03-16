new_list = [1,2,3]

result = new_list[0] # Access is a constant time operation O(1)

# "in" operator is used to check if an element is present in a list/array

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break

# Most array implementations support three types of insert operations:
# Insert: Adds an element at a specific index position, its more costly than appending because python has to shift all the elements to the right of the index position, linear time operation
# Appending: Adds an element to the end of the array, constant time operation
# Extend: Adds multiple elements to the end of the array, linear time operation
# Delete : Removes an element from a specific index position, its more costly than removing the last element because python has to shift all the elements to the left of the index position, linear time operation

numbers = []
numbers.extend([1,2,3,4,5])
print(numbers)

# video 2:23:05