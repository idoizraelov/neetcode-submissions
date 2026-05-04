class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    count+=1
        
        time=0
        while count>0 and q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in direct:
                    row,col=r+dr,c+dc
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                        grid[row][col]=2
                        q.append((row,col))
                        count-=1
            time+=1    
                    
        return time if count==0 else -1