"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None

        curr = head

        # Create new
        while curr:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        
        # Fill in random pointer value
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Separate the lists
        curr = head
        newHead = head.next
        newCurr = newHead
        while curr:
            curr.next = newCurr.next
            curr = curr.next
            if curr:
                newCurr.next = curr.next
                newCurr = newCurr.next
        
        return newHead




