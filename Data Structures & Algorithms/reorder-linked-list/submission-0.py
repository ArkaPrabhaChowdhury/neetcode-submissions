# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev=slow.next = None
        
        # Reverse from middle
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first = head
        second = prev

        # Merge the two lists
        while second:
            tempf = first.next
            temps = second.next
            first.next = second
            second.next = tempf
            first = tempf
            second = temps