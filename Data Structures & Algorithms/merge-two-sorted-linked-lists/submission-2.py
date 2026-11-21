# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        #dummyNode = dummyNode.next
        res = dummyNode

        while list1 or list2:

            if list1 and list2:
                if list1.val > list2.val:
                    dummyNode.next = list2
                    list2 = list2.next
                else:
                    dummyNode.next = list1
                    list1 = list1.next

            elif list1 and not list2:
                dummyNode.next = list1
                list1 = list1.next

            else:
                dummyNode.next = list2
                list2 = list2.next

            dummyNode = dummyNode.next
        return res.next

