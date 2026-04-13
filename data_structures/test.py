class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

counter = 0
a = 8
total = a * 2 + counter
counter  = total // 10

print(total % 10, counter)