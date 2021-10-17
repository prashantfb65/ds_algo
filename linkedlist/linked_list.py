

class Node:

    def __init__(self, element) -> None:
        self.element = element
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.lsize = 0
    
    def print_ll(self):
        current = self.head
        while current:
            print(current.element, end=">")
            current = current.next
        print()
    
    def insert(self, element, position):
        if position == 0:
            self.insert_at_end(element)
        elif position == 1:
            self.insert_at_front(element)
        else:
            raise ValueError("Invalid position passed, valid options: 0 for beginning  and 1 for end")

    def insert_at_end(self, element):
        new_element = Node(element)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
        self.lsize += 1
    
    def insert_at_front(self, element):
        new_element = Node(element)
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element
        self.lsize += 1
    
    def size(self):
        return self.lsize

    def is_empty(self):
        return self.lsize == 0

    def add_sample_elements(self, elements = [], front=0):
        for el in elements:
            self.insert(el, front)
        
    def reverse(self):
        previous = None
        while self.head:
            temp = self.head
            self.head = self.head.next
            temp.next = previous
            previous = temp 
        self.head = previous   
    