# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        current=head

        while current:
            count+=1
            current=current.next
            
        length=count

        target=count-n
        if target==0:
            head=head.next
            return head

        current=head
        for i in range(target-1):
            current=current.next

        current.next=current.next.next
        return head
        