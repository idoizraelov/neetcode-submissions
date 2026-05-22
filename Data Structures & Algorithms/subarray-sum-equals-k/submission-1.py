class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_sum,count=0,0
        dic={0:1}
        for i in range(len(nums)):
            sub_sum+=nums[i]
            if sub_sum-k in dic:
                count+=dic[sub_sum-k]
            dic[sub_sum]=dic.get(sub_sum,0)+1
        
        return count
        
        
