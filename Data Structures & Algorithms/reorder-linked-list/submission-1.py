# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        fast=slow.next
        slow.next=None

        prev=None
        current = fast

        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        l1=head
        l2=prev

        while l2:
            a=l1.next
            b=l2.next
            l1.next=l2
            l2.next=a
            l1=a
            l2=b









        