class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        sum_left=0
        for i, num in enumerate(nums):
            sum_right=total-sum_left-num
            if sum_left == sum_right:
                return i
            sum_left+=num

        return -1
           

