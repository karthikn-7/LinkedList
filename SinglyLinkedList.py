class Node:
    def __init__(self, element):
        self.element = element
        self.pointer = None




class Linked_list:
    """
    My own implementation of linked list it gives me so much idea
    methods:add
            head
            insert
            insert_at_end
            insert_at_front
            length
            remove
            search_element
            searching
            traversal
    """
    def __init__(self):
        self.head = None #Initializing the head.

    def add_element(self, data)->None:
        """Adds element in the list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while(cur.pointer is not None):
                cur = cur.pointer

            cur.pointer = new_node
            
    # Remove the element from the list
    def remove_element(self, data) -> None:
        """Remove element from the list"""
        if self.head.element == data:
            self.head = self.head.pointer
        else:
            cur = self.head
            while(cur.pointer is not None):
                element = cur.pointer.element
                if element == data:
                    cur.pointer = cur.pointer.pointer
                # setting the pointer object to the cur variable
                cur = cur.pointer
    
    def length(self):
        """Returns the non-zero based index"""
        count = 0
        head = self.head
        while(head is not None):
            head = head.pointer
            count+=1 #Incrementing the count variable
        return count

    # Optional no use method for inserting at the end, this can also able to do by add method
    def insert_at_end(self,data):
        new_node = Node(data)
        head = self.head
        cur = head
        while (cur.pointer is not None):
            cur = cur.pointer
        # inserting the element in the last position of the list
        cur.pointer = new_node
        inserted_node_object = cur.pointer
        return inserted_node_object

    # This method is used to add element at the first position of the list
    def insert_at_front(self, data) -> None:
        """Insert element at the beginning of the list"""
        new_node = Node(data)
        new_node.pointer = self.head
        self.head = new_node

    # Method to insert element at the specific position of the list
    def insert_element(self, data, index) -> None:
        """Insert element at any position index needed"""
        new_node = Node(data)
        head = self.head
        cur = head
        if(index == 0):
            self.insert_at_front(data)
            return
        count = 1
        while (cur is not None and count != index):
            cur = cur.pointer
            count+=1
        if(cur is None):
            raise IndexError("Index is greater than the length of list")
            return
        new_node.pointer = cur.pointer
        cur.pointer = new_node

    def search_element(self, data) -> bool:
        """Search the element in the list if found return True"""
        cur = self.head
        while (cur is not None):
            if (cur.element == data):
                return True
            cur = cur.pointer
        return False

    def reverse(self):
        head = self.head
        prev = None
        cur = head
        while cur is not None:
            second_node = cur.pointer
            cur.pointer = prev
            prev = cur
            cur = second_node
        
        self.head = prev

    def traverse(self) -> None:
        """Traverse throught the all element"""
        cur = self.head
        while (cur is not None):#if the pointer of head is not none.
            print(cur.element)
            cur = cur.pointer 






# singly linked list manual operation
ll = Linked_list()
ll.add_element(10)
ll.add_element(20)
ll.add_element(30)
ll.add_element(40)
ll.add_element(50)
ll.add_element(60)


import random

