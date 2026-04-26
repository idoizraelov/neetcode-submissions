class Solution:
    def maxDifference(self, s: str) -> int:
        count=Counter(s)
        max_odd=0
        min_even=float("inf")
        for val in count.values():
            if val%2==0:
                min_even=min(min_even,val)
            else:
                max_odd=max(max_odd,val)
    
        return max_odd-min_even