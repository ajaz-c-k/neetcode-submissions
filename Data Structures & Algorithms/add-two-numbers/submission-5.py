# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        dummy=node
        tail=node
        a=l1
        b=l2
        carry=0

        while a or b:
            if a==None :
                a_val=0
            else:
                a_val=a.val
            if b == None:
                b_val=0
            else:
                b_val=b.val
            total = a_val+b_val+carry
            digit = total%10
            carry = total // 10

            a=a.next if a else None
            b=b.next if b else None

            node=ListNode(digit)
            tail.next=node
            tail=tail.next

        if carry:
            node=ListNode(carry)
            tail.next=node

        return dummy.next



        