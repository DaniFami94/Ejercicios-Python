#we create a class to represent a node

class Node:
    """
    An object for storing a single node of a linked list.
    Models two atrributes - data and the link to the next node in the list
    """
    def __init__(self, data): #constructor to initialize the node with data
        self.data = data #data stored in the node
        self.next_node = None #pointer to the next node in the list

    def __repr__(self): 
        return f"<Node data: {self.data}>" #string representation of the node
        
class LinkedList: # We create a class to represent the linked list
    """
    Singly linked list
    """
    def __init__(self):
        
        self.head = None #initialize the head of the linked list
    
    def is_empty(self): #check if the linked list is empty
        
        return self.head == None


    def size(self): 
        """
        Returns the number of nodes in the linked list
         Takes O(n) time "Linear time"
         """
        current = self.head #initialize the current node to the head of the linked list
        count = 0   #initialize a counter to keep track of the number of nodes in the linked list

        while current: #loop through the linked list until the current node is None
            count = count + 1 #increment the counter
            current = current.next_node #move to the next node
        
        return count #return the number of nodes in the linked list

    def add(self, data):
        """
        Add a new node containing data at the head of the linked list
        Takes O(1) time "Constant time"
        """
        new_node = Node(data) #create a new node
        new_node.next_node = self.head #set the next node of the new node to the head of the linked list
        self.head = new_node #set the head of the linked list to the new node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found
        Takes O(n) time "Linear time"
        """
        current = self.head #initialize the current node to the head of the linked list

        while current: #while the current node is not None
            if current.data == key: #check if the data in the current node matches the key
                return current #return the current node if the data matches the key
            else:
                current = current.next_node #move to the next node
        return None #return None if the key is not found
    
    def insert(self,data,index):
        """
        Insert a new node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion point takes O(n) time
        Takes overall O(n) time "Linear time"
        """
        if index == 0:
            self.add(data) #add the data at the head of the linked list

        if index > 0:
            new = Node(data)  #create a new node
            
            position = index #initialize the position to the index
            
            current = self.head #initialize the current node to the head of the linked list

            while position > 1: #loop through the linked list until the position is greater than 1
                current = current.next_node #move to the next node
                position = position - 1 #decrement the position
        
        prev_node = current #store the current node in a variable
        
        next_node = current.next_node #store the next node in a variable
        
        prev_node.next_node = new #set the next node of the previous node to the new node
        
        new.next_node = next_node #set the next node of the new node to the next node

    def remove(self,key):
        """
        Remove the first node containing data that matches the key
        Returns the node or None if the key is not found
        Takes O(n) time "Linear time"
        """
        current = self.head #initialize the current node to the head of the linked list
        previous = None #initialize the previous node to None
        found = False # found is going to serve as a stopping condition for the loop

        while current and not found: #loop through the linked list until the current node is None or the key is found
           
           if current.data == key and current is self.head: #check if the data in the current node matches the key and the current node is the head of the linked list
               
               found = True 
               
               self.head = current.next_node #set the head of the linked list to the next node of the current node
            
           elif current.data == key: #check if the data in the current node matches the key
                    
                    found = True 
                    
                    previous.next_node = current.next_node #set the next node of the previous node to the next node of the current node

           else: #if the key is not found
               
               previous = current #set the previous node to the current node
               current = current.next_node #move to the next node

        return current #return the current node


    def __repr__(self): #string representation of the node
        """
        Returns a string representation of the linked list node
        Takes O(n) time "Linear time"
        Python's `is` operator checks for identity (if two variables point to the exact same object in memory), is equivalent to the === operator in JavaScript
        """

        nodes = [] # initialize an empty list to store the nodes in the linked list
        current = self.head # initialize the current node to the head of the linked list

        while current: # loop through the linked list until the current node is None
            if current is self.head: # check if the current node is the head of the linked list
                nodes.append("[Head: %s]" %current.data) # append the head of the linked list to the nodes list
            elif current.next_node is None: # check if the next node of the current node is None
                nodes.append("[Tail: %s]" %current.data) # append the tail of the linked list to the nodes list
            else:
                nodes.append("[%s]" %current.data) # append the current node to the nodes list
            current = current.next_node # move to the next node
        return '->'.join(nodes) # return the nodes in the linked list as a string




#video 3:03:09