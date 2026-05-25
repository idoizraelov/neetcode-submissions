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
        
        temp=head
        dic={None:None}
        while temp:
            dic[temp]=Node(temp.val)
            temp=temp.next

        temp =head
        while temp:
            curr=dic[temp]
            curr.next=dic[temp.next]
            curr.random=dic[temp.random]
            temp=temp.next
        
        return dic[head]



