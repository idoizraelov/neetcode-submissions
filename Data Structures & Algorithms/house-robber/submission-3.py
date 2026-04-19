class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=nums[0]
        n=len(nums)
        if n==1 : return nums[0]
        curr=max(nums[0],nums[1])
        for i in range(2,n):
            result=max(prev+nums[i],curr)
            prev=curr
            curr=result
        
        return curr
