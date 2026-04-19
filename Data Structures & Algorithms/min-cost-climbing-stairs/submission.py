class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        prev=cost[0]
        curr=cost[1]
        for i in range(2,n):
            result=min((curr+cost[i]),(prev+cost[i]))
            prev=curr
            curr=result

        return min(curr,prev)