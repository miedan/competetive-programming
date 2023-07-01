# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

             
            dummy1, dummy2 = ListNode(), ListNode()
            d1, d2 = dummy1, dummy2
            while head:
                if head.val < x:
                    d1.next = head
                    d1 = d1.next
                else:
                    d2.next = head
                    d2 = d2.next
                head = head.next
                
            d1.next = dummy2.next
            d2.next = None
            return dummy1.next