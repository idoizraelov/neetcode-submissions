class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        rows = len(matrix)
        cols =len(matrix[0])

        left=0
        right= rows*cols-1
        while left<=right:
            mid=(right+left)//2

            row=mid//cols
            col=mid%cols
            val = matrix[row][col]

            if val==target:
                return True 
            else:
                if val>target:
                    right=mid-1
                else:
                    left=mid+1
        
        return False 