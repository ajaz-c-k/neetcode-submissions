# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        before=dummy

        current =head
        prev = None
       

        for i in range(left-1):
            before = current
            current=current.next
        rev_count=right-left+1
        left_node=current

        for i in range(rev_count):
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        before.next=prev
        left_node.next=current

        return dummy.next
        