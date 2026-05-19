class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        q=deque()
        rows=len(board)
        cols=len(board[0])
        for i in range(rows):
            if board[i][0]=="O":
                q.append((i,0))
                board[i][0]="T"
            if board[i][cols-1]=="O":
                q.append((i,cols-1))
                board[i][cols-1]="T"
        for i in range(cols):
            if board[0][i]=="O":
                q.append((0,i))
                board[0][i]="T"
            if board[rows-1][i]=="O":
                q.append((rows-1,i))
                board[rows-1][i]="T"
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dirs:
                    row,col=r+dr,c+dc
                    if row in range(rows) and col in range(cols) and board[row][col]=="O":
                        board[row][col]="T"
                        q.append((row,col))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"

                    
