    
class LinkedList:   
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val      # значение (что человек держит)
            self.next = next    # ссылка на следующего (за кого держится)
        def __repr__(self) -> str:
            pass

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def create_list(self, arr):
        if not arr: return None
        self.head = self.ListNode(arr[0])
        current = self.head
        for val in arr[1:]:
            current.next = self.ListNode(val)
            current = current.next
        self.tail = current
        return self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" → ")
            current = current.next
        print("None")

    def add_first(self, value):
        new_node = self.ListNode(value)
        if not self.head:
            return new_node
        
        new_node.next = self.head
        self.head = new_node
        return self.head

    def append(self, val):
        new_node = self.ListNode(val)
        if not self.head:
            self.head = self.tail = new_node
            return self.head
        self.tail.next = new_node
        self.tail = new_node
        return self.head

    def __len__(self):  
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    
    def delete(self, val):
        if self.head and self.head.val == val:
            return self.head.next
        
        current = self.head
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next 
                #return self.head
            current = current.next
        return self.head

arr = [1, 2, 2, 3, 4, 5]

s = LinkedList()
s.create_list(arr)
s.print_list()
s.add_first(7)
s.print_list()

s.delete(2)
s.print_list()


