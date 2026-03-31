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
        deepCopy = {None:None}

        curr1 = curr = head
        while curr:
            copy = Node(curr.val)
            deepCopy[curr] = copy
            curr = curr.next
        
        while curr1:
            copy = deepCopy[curr1]
            copy.next = deepCopy[curr1.next]
            copy.random = deepCopy[curr1.random]
            curr1 = curr1.next
        
        return deepCopy[head]