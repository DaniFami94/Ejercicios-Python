```python

# Data Structure it is the collection of values and the format they are stored in, the relationships between the values in the collection as well as the operations applied on the data stored in the structure

# Operations on Data Structures

- Access and read values

- Search for an arbitrary values

- Insert values at any point into the structure

- Dekete values in the structure

`Array`: is a data structure that stores a collection of values where each value is referenced using a index or a key.

# Most array implementations support three types of insert operations:
- Insert: Adds an element at a specific index position, its more costly than appending because python has to shift all the elements to the right of the index position, linear time operation

- Appending: Adds an element to the end of the array, constant time operation

- Extend: Adds multiple elements to the end of the array, linear time operation

`Linked List`: is linear data structure with each element in the list is contained in a separate object called node. A node models two pieces of imformation an individual item of the data we want to store, and a reference to the next node in the list. The first node in the linked list is called the head of the list while the last node is called the tail. Nodes are also know as self referential objects this means that a node includes a link to another node. The last node "the tail" does not link to anything. We can insert a node at any point in the linked list in constant time.
