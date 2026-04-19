class Solution:
    def simple_rob(self,sub_list):
        n = len(sub_list)
        if n == 0: return 0
        if n == 1: return sub_list[0]
        prev=sub_list[0]
        curr=max(sub_list[0],sub_list[1])
        for i in range(2,n):
            result=max(prev+sub_list[i],curr)
            prev=curr
            curr=result
            
        
        return curr

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        res1 = self.simple_rob(nums[:-1])
        res2 = self.simple_rob(nums[1:])
        
        return max(res1, res2)
