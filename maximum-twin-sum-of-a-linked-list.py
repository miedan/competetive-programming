# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        max_sum = 0

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        hold = slow
        slow = slow.next
        tmp = slow
        

        while slow :
            tmp = slow
            slow = slow.next
            tmp.next = prev
            prev = tmp
        hold.next = prev 
        prev = prev
        cur = head

        while prev:
            max_sum = max(max_sum, prev.val + cur.val)
            cur = cur.next
            prev = prev.next
        
        return max_sum