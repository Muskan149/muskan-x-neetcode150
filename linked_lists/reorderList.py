# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # get to the middle of the list 
        mid = slow
        print(f"found mid: {mid.val}")

        # mid.next is the start of the second half 
        prev, curr = None, mid.next 

        mid.next = None
        
        # reverse the second half: keep track of its head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge both arrays alternatively
        # have a dummy pointer that points to result pointer
        # while result is a valid node: make result point to head            

        res = ListNode(0)

        first, second = head, prev

        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        





        

        
