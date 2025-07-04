# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy
        
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            # while both curr1 and curr2 havent ended
            # take the greater of both the nodes and make res point to it
            # if curr1 is bigger: update curr1 to next
            # if curr2 is bigger: update curr2 to next
            if curr1.val < curr2.val: # curr 1 is smaller
                res.next = curr1
                res = res.next
                curr1 = curr1.next
            elif curr2.val < curr1.val: # curr2 is smaller
                res.next = curr2
                res = res.next
                curr2 = curr2.next
            else: 
                res.next = curr1
                res = res.next
                curr1 = curr1.next
                res.next = curr2
                res = res.next
                curr2 = curr2.next

        # if only list1 exists:
        # res.next => curr1; break
        if curr1:
            res.next = curr1

        # if only list2 exists:
        # res.next => curr2; break
        if curr2:
            res.next = curr2
        
        return dummy.next






        
