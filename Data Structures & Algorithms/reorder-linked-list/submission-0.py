# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = cur = ListNode()
        temp = head
        values = []
        head = head.next
        while head:
            values.append(head.val)
            head = head.next
        
        head = temp
        head = head.next
        i = 0
        while values:
            
            head.val = values.pop() if i % 2 == 0 else values.pop(0)
            if head:
                head = head.next
            i +=1
