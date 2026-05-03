class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            hour=0
            for i in piles:
                hour+=(i+k-1)//k
            return hour
            
        left=1
        right=max(piles)
        
        while left<right:
            mid=(right+left)//2
            if check(mid) > h:
                left=mid+1
            else:
                right=mid
        
        return left
