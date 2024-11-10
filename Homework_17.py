########################################
#Homework_17 Task_1
########################################
# Node class represents a single node in a linked list
class Node:
    def __init__(self, data=None):
        self.data = data  # Stores the data for the node
        self.next = None  # Pointer to the next node in the list


# LinkedList class handles operations for a linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initializes the linked list with no head (empty list)

    # Method to add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # Check if the list is empty
            self.head = new_node  # If empty, make the new node the head of the list
            return

        # Traverse to the last node in the list
        last_node = self.head
        while last_node.next:  # Loop until reaching the end of the list
            last_node = last_node.next

        last_node.next = new_node  # Link the new node to the end of the list

    # Method to remove a node at a specific index
    def remove_at(self, index):
        if index < 0 or self.head is None:  # Check if index is invalid or the list is empty
            return

        if index == 0:  # Special case for removing the head node
            self.head = self.head.next  # Move the head pointer to the next node
            return

        # Traverse to the node before the one to be removed
        current_node = self.head
        current_position = 0

        while current_node.next and current_position < index - 1:
            current_node = current_node.next  # Move to the next node
            current_position += 1  # Update the current position

        # Link the previous node to the node after the one being removed (if it exists)
        if current_node.next:
            current_node.next = current_node.next.next

    # Method to display the elements in the list
    def display(self):
        current_node = self.head  # Start from the head node
        while current_node:  # Continue until the end of the list
            print(current_node.data, end=' -> ')  # Print the data of each node
            current_node = current_node.next  # Move to the next node
        print()  # Print a newline at the end


# Instantiate a LinkedList object
linked_list = LinkedList()

# Append values to the linked list
linked_list.append(50)  # 0
linked_list.append(15)  # 1
linked_list.append(20)  # 2
linked_list.append(11)  # 3
linked_list.append(5)   # 4
linked_list.append(25)  # 5

# Display the list after adding elements
linked_list.display()  # Output: 50 -> 15 -> 20 -> 11 -> 5 -> 25 ->

# Remove the node at index 2 and display the list
linked_list.remove_at(2)
linked_list.display()  # Output: 50 -> 15 -> 11 -> 5 -> 25 ->

# Remove the node now at index 2 and display the list
linked_list.remove_at(2)
linked_list.display()  # Output: 50 -> 15 -> 5 -> 25 ->

# Remove the head node (index 0) and display the list
linked_list.remove_at(0)
linked_list.display()  # Output: 15 -> 5 -> 25 ->

# Remove the node now at index 2 and display the list
linked_list.remove_at(2)
linked_list.display()  # Output: 15 -> 5 ->


############################################


############################################
#Homework_17 Task_2
############################################
# Node class represents a single node in the stack
class Node:
    def __init__(self, data=None):
        self.data = data      # Stores the data for the node
        self.next = None      # Pointer to the next node (used in linked list structure)

# Stack class represents a stack data structure using a linked list
class Stack:
    def __init__(self):
        self.top_node = None  # Pointer to the top node in the stack (initially empty)
        self.length = 0       # Track the number of elements in the stack

    # Method to check if the stack is empty
    def empty(self):
        return self.length == 0  # Returns True if the stack has no elements

    # Method to get the current size of the stack
    def size(self):
        return self.length       # Returns the number of elements in the stack

    # Method to add an element to the top of the stack
    def push(self, data):
        new_node = Node(data)    # Create a new node with the given data
        new_node.next = self.top_node  # Link the new node to the previous top node
        self.top_node = new_node  # Update the top of the stack to be the new node
        self.length += 1          # Increment the stack size by 1

    # Method to remove and return the top element of the stack
    def pop(self):
        if not self.empty():  # Check if the stack is not empty
            popped_item = self.top_node.data  # Store the data of the top node
            self.top_node = self.top_node.next  # Move the top pointer to the next node
            self.length -= 1       # Decrement the stack size by 1
            return popped_item     # Return the popped data
        else:
            raise IndexError("Stack is empty")  # Raise an error if the stack is empty


# Test cases to demonstrate Stack functionality
stack = Stack()

# Check if the stack is empty and its initial length
print(stack.empty())  # Output: True, since stack is initially empty
print(stack.length)   # Output: 0, as the stack is empty

# Pushing values onto the stack
stack.push(200)
stack.push(50)
stack.push(75)
stack.push(25)
stack.push(30)

# Check if the stack is empty and its length after pushing elements
print(stack.empty())  # Output: False, stack now contains elements
print(stack.length)   # Output: 5, as there are five elements in the stack

# Popping elements from the stack
print(stack.pop())    # Output: 30 (last pushed, so it's at the top)
print(stack.empty())  # Output: False, stack still has elements
print(stack.length)   # Output: 4, one element removed

print(stack.pop())    # Output: 25
print(stack.length)   # Output: 3

print(stack.pop())    # Output: 75
print(stack.length)   # Output: 2

print(stack.pop())    # Output: 50
print(stack.length)   # Output: 1

print(stack.pop())    # Output: 200 (last remaining element)
print(stack.empty())  # Output: True, stack is now empty
print(stack.length)   # Output: 0

# Trying to pop from an empty stack will raise an error
print(stack.pop())    # Raises IndexError: "Stack is empty"

############################################

############################################
#Homework_17 Task_3
############################################
# Node class represents a single node in a linked list
class Node:
    def __init__(self, data=None):
        self.data = data  # Stores the data of the node
        self.next = None  # Pointer to the next node in the list

# LinkedList class for managing the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list, no nodes

    # Method to display the list contents for testing and visualization
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()

    # Method to remove the first occurrence of a value from the list
    def remove_by_value(self, value):
        current_node = self.head

        # Case 1: If the list is empty
        if current_node is None:
            print("List is empty")
            return

        # Case 2: If the head node contains the value
        if current_node.data == value:
            self.head = current_node.next
            return

        # Case 3: Traverse the list to find the value
        while current_node.next:
            if current_node.next.data == value:
                current_node.next = current_node.next.next  # Remove the node
                return
            current_node = current_node.next

        print("Value not found in the list")

    # Method to append a node at a specific index
    def append_by_index(self, index, data):
        new_node = Node(data)

        # Case 1: If index is 0, insert at the beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_position = 0

        # Traverse the list to find the node just before the index
        while current_node and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        # Case 2: If index is out of bounds
        if current_node is None:
            print("Index is out of bounds")
            return

        # Case 3: Insert at the specified index
        new_node.next = current_node.next
        current_node.next = new_node

# Example usage of LinkedList with remove_by_value and append_by_index methods
linked_list = LinkedList()

# Adding elements using append by index
linked_list.append_by_index(0, 10)  # List: 10
linked_list.append_by_index(1, 20)  # List: 10 -> 20
linked_list.append_by_index(2, 30)  # List: 10 -> 20 -> 30
linked_list.append_by_index(1, 15)  # List: 10 -> 15 -> 20 -> 30

print("List after append operations:")
linked_list.display()

# Removing a value (15) from the list
linked_list.remove_by_value(15)  # List: 10 -> 20 -> 30
print("List after removing value 15:")
linked_list.display()

# Attempting to remove a value that doesn't exist (100)
linked_list.remove_by_value(100)  # Output: "Value not found in the list"


########################################


