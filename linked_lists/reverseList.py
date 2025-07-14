class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # make a list with the elements
        # head = list.pop()
        # while list: head.next = head.pop
        prev, curr = None, head

        dummy = ListNode()
        dummy.next = curr

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

        
            
            
