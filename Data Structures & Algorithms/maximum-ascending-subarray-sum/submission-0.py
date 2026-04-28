class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum_inc=max_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sum_inc+=nums[i]
            else:
                sum_inc=nums[i]
            max_sum=max(max_sum,sum_inc)
        
        return max_sum