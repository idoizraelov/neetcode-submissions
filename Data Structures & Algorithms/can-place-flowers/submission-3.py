class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        length=len(flowerbed)
        while n>0 and i<length:
            if flowerbed[i]==1:
                i+=2
            else:
                if i+1 == length or flowerbed[i+1]==0:
                    n-=1
                    i+=2
                else:
                    i+=1
        return n==0