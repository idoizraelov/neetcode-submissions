class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0<nums[i]<=len(nums) and nums[i] != nums[nums[i]-1]:
                curr=nums[i]-1
                nums[curr],nums[i]=nums[i],nums[curr]
        print(nums)
        i=0
        while i<len(nums) and nums[i]>0 and nums[i] == i+1:
                i+=1
        
        return i+1