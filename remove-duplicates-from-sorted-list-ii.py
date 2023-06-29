# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        cur = head
        prev = dummy
        
        while cur and cur.next:

            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    
                    cur = cur.next
                cur = cur.next
                prev.next = cur
            else:
                
                prev = cur
                cur = cur.next

        return dummy.next