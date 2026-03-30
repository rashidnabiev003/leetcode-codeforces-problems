class LinkedList:
    class ListNode:
        def __init__(self, value=0, next=None):
            self.value = value
            self.next = next
        def __repr__(self) -> str:
            return f"{self.value}"

    def __init__(self) -> None:
        self.__head = None
        self.__tail = None

    def add_first(self, value):
        new_node = self.ListNode(value)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            new_node.next = self.__head
            self.__head = new_node
    
    def add_last(self, value):
        new_node = self.ListNode(value)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            self.__tail.next = new_node
            self.__tail = new_node
    
    def remove_first(self):
        if self.__is_empty():
            raise ValueError("List is empty")
        
        removed_value = self.__head.value
        if self.__has_one_node():
            self.__reset()
        else:
            self.__head = self.__head.next
        return removed_value
    
    def remove_last(self):
            if self.__is_empty():
                raise ValueError("List is empty")
            
            removed_value = self.__tail.value
            
            if self.__has_one_node():
                self.__reset()
            else:
                current = self.__head
                while current.next != self.__tail:  
                    current = current.next
                
                current.next = None  
                self.__tail = current
            
            return removed_value

    def remove(self, value):
        if self.__is_empty():
            raise ValueError("LinkedList is empty")

        if self.__head.value == value:
            self.remove_first()
            return
        if self.__tail.value == value:
            self.remove_last()
            return

        current = self.__head
        prev = self.__head
        while current.next:
            if current.value == value:
                prev.next = current.next
                current.next = None
                return 
            prev = current
            current = current.next
        
        raise ValueError("Not in List")    
    
    def nth_node(self, value):
        if self.__is_empty() or (self.__has_one_node() and value == 1):
            raise ValueError
        
        if value == 0:
            return self.__tail
        
        current = self.__head
        for _ in range(value):
            current = current.next
        
        prev = self.__head
        while current.next:
            prev = prev.next
            current = current.next
        
        return prev.value

    def __reset(self):
        self.__head = self.__tail = None

    def __has_one_node(self):
        return self.__head == self.__tail

    def __is_empty(self):
        return self.__head is None

    def __initialize(self, new_node):
        self.__head = self.__tail = new_node

s = LinkedList()
s.add_last(10)
s.add_last(20)
s.add_last(50)
s.add_last(70)
s.add_last(30)
print(s)