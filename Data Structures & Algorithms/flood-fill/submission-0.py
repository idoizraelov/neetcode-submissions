class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color: 
            return image
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        orig=image[sr][sc]
        q = deque([(sr, sc)])
        image[sr][sc]=color
        
        while q:
            r,c=q.popleft()
            for dr,dc in dirs:
                row,col=r+dr,c+dc
                if row in range(len(image)) and col in range(len(image[0])) and image[row][col] == orig:
                    q.append((row,col))
                    image[row][col]=color                    
                
        return image