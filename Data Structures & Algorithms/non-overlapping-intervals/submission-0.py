class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort(key=lambda i: i[1])
        for i in range(1,len(intervals)):
            
            if intervals[i-1][1]>intervals[i][0]:
                count+=1
                intervals[i][1]=intervals[i-1][1]
        
        return count