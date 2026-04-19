from typing import List

class ListNode:
    def __init__(self,val: int)->None:
        self.val=val
        self.next=None



class LinkedList:
    
    def __init__(self):
        self.head = None 
        self.tail = None
    
    def get(self, index: int) -> int: 
        if index < 0 :
            return -1
        curr = self.head
        count=0
        while curr:
            if count == index:
                return curr.val
            curr= curr.next
            count+=1
        return -1
        

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head=ListNode(val)
            self.tail=self.head
        else:
            temp= ListNode(val)
            temp.next=self.head
            self.head=temp


    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head=ListNode(val)
            self.tail=self.head
        else:
            temp= ListNode(val)
            self.tail.next=temp
            self.tail=temp

    def remove(self, index: int) -> bool:
        if index < 0 :
            return False
        if not self.head:
            return False 
        if 0==index:
            if self.head == self.tail:
                self.tail = None
            self.head=self.head.next
            return True 
        curr = self.head.next
        prev =self.head
        count=1
        while curr:
            if count == index:
                if curr == self.tail:
                    self.tail = prev
                prev.next =curr.next
                return True
            prev=curr
            curr= curr.next
            count+=1
        return False 

    def getValues(self) -> List[int]:
        arr=[]
        curr=self.head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        return arr
