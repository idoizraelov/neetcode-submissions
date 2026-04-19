class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length=0
        self.arr=[0]*capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i>=0 and i<self.length:
            self.arr[i]=n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length]=n
        self.length+=1

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        new_arr=[0]*2*len(self.arr)
        for i in range (0,self.capacity):
            new_arr[i]=self.arr[i]
        self.arr=new_arr
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
