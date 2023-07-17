class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        current = self.head
        start = 1
        if self.head:
            while current:
                if start == position:
                    return current
                else:
                    current = current.next
                    start += 1
                    
        return None
    
    def insert(self, new_element, position):
        if self.head:
            before_elem = self.get_position(position - 1)
            new_element.next = before_elem.next
            before_elem.next = new_element
        else:
            self.head = new_element
        pass
    
    
    def delete(self, value):
        current = self.head
        
        if self.head:
            while current:
                if current.value == value:
                    self.head = current.next
                    return
                current = current.next
                
        pass
