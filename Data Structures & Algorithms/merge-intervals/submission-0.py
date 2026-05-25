class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort(key=lambda x:x[0])
        interval=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= interval[1]:
                interval[1]=max(intervals[i][1],interval[1])
            else:
                res.append(interval)
                interval=intervals[i]
        res.append(interval)
        return res



            