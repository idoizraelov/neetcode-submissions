# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        fast=head.next
        slow=head
        #find the middle
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        #breack the second half
        second=slow.next
        slow.next=None
        #Reverse the second half
        prev=None
        curr=second
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        #merge the two halves
        first=head
        second=prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            second=temp2
            first=temp1
        
            
        
        
        


            

        