class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direct=[[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands=0

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            grid[r][c]="0"
            
            while q:
                r,c=q.popleft()
                for dr ,dc in direct:
                    row,col=r+dr,c+dc
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]=="1":
                        q.append((row,col))
                        grid[row][col]="0"
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1

        return islands
