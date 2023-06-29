# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        if k == 0:
            return head
            
        prev = None
        dummy = ListNode(0, head)

        n = 1
        temp = head
         
        while temp.next:

            temp = temp.next
            n += 1

        last = temp

        k = k % n
        

        prev, cur = None, head

        for i in range(n - k - 1):

            cur = cur.next
        
        last.next = dummy.next
        dummy.next = cur.next 
        cur.next = prev

        return dummy.next