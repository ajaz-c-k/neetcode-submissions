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
        current=head
        copy={}
        if not head:
            return None

        while current:
            new_node=Node(current.val)
            copy[current]=new_node
            current=current.next  

        current=head

        while current:
            new_node=copy[current]
            if current.next:
                new_node.next=copy[current.next]
            else:
                new_node.next=None
            if current.random:
                new_node.random=copy[current.random]
            else:
                new_node.random=None
            current=current.next
        return copy[head]   

        