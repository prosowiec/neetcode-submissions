# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        cur = head
        listVals = []

        while cur:
            listVals.append(cur.val)
            cur = cur.next

        print(listVals)
        i = 0
        while head:
            if i % 2 == 1:
                head.val = listVals.pop()
            else:
                head.val = listVals.pop(0)
            head = head.next

            i+=1
