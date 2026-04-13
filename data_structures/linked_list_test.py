    
class LinkedList:   
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val      # значение (что человек держит)
            self.next = next    # ссылка на следующего (за кого держится)

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

    def is_pallindrome(self) -> bool:
        prev = None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow 
        while current:
            next_tmp = current.next
            current.next = prev
            prev = current
            current = next_tmp
        
        current = self.head
        while prev:
            if current.val != prev.val:
                return False
            else:
                current = current.next
                prev = prev.next
        
        return True

    def binary(self) -> int:
        current = self.head
        s = ''
        while current:
            s += str(current.val)
            current = current.next
        
        return int(s, 2)

    def double_it(self):
        prev = None
        current = self.head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        counter = 0
        current = self.head

        while current:
            total = current.val * 2 + counter
            counter = total // 10
            current.val = total % 10
            prev = current
            current = current.next
        
        if counter:
            prev.next = self.ListNode(1)
        
        new_prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = new_prev
            new_prev = current
            current = temp
        
        self.head = new_prev
        return self.head
    
    def bit_to_int(self):
        s = ''
        current = self.head
        while current:
            s += str(current.val)
            current = current.next
        
        return int(s, 2)
    
    def rotate_linked_list(self, k):
        linkedlist_len = 1

        tail = self.head
        while tail.next:
            linkedlist_len += 1
            tail = tail.next
        
        tail.next = self.head
        k = k % linkedlist_len

        new_tail = self.head
        for _ in range(linkedlist_len - k - 1):
            new_tail = new_tail.next
        
        self.head = new_tail.next
        new_tail.next = None
    
    def swap_nodes_val(self, k):
        slow = fast = self.head
        for _ in range(k-1):
            fast = fast.next
        first_node = fast

        while fast.next:
            slow = slow.next
            fast = fast.next

        second_node = slow

        first_node.val, second_node.val = second_node.val, first_node.val
    
    def remove_duplicates_from_sorted_list(self):
        slow = self.head
        fast = self.head.next

        while fast:
            if slow.val == fast.val:
                slow.next = None
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next

    def remove_all_duplicates_from_sorted_list(self):
        dummy_node = self.ListNode()
        dummy_node.next = self.head
        prev = dummy_node
        current = self.head

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                
                prev.next = current.next
            else:
                prev = prev.next
            
            current = current.next
        
        self.head = dummy_node.next

    
    def merge_two_lists(self, list1, list2):
        dummy_node = self.ListNode(0)
        current = dummy_node

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        current.next = list1 if list1 else list2

        return dummy_node.next
    
    def sort(self, head):
        if not head or not head.next:
            return head
        
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None

        left  = self.sort(head)
        right = self.sort(slow)

        return self.merge_two_lists(left, right)
    
    def sort__(self):
        self.head = self.sort(self.head)





arr = [2, 3, 4, 5, 1]

s = LinkedList()
s.create_list(arr)
s.print_list()
s.sort__()
s.print_list()

