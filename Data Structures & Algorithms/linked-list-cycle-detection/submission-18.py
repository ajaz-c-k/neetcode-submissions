# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        if not head:
            return False

        if not head.next:
            return False
        while head.next.next != None:
            head = head.next.next 
            if not head.next:
                return False
           
            if curr == head:
                return True

            else:
                curr = curr.next
        return False