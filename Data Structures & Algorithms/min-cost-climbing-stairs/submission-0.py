class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        arr=[float('inf')]*(n)
        arr[0]=cost[0]
        arr[1]=cost[1]
        for i in range(2,n):
            arr[i]=min((arr[i-1]+cost[i]),(arr[i-2]+cost[i]))

        return min(arr[n-1],arr[n-2])