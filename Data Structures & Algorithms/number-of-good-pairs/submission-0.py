class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res=0 
        dic={}
        for num in nums:
            if num in dic:
                res+=dic[num]
                dic[num]+=1
            else:
                dic[num]=1
        return res