# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        pos = 0

        curr = head

        while curr:
            length+=1
            curr = curr.next

        pos = length - n

        curr = head 

        if pos == 0:
            head = head.next
            return head
        while curr:
            pos-=1
            if curr.next == None:
                return None
            print(pos)
            if pos==0:
                curr.next = curr.next.next
                return head
            curr = curr.next
            

        

