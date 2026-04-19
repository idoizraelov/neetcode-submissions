class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0
        col =len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]>target:
                col-=1
            else:
                row+=1
            
        return False 
    '''
    def search_bin(arr,target):
        left=0
        right=len(arr)-1
        while left<right:
            mid=(right+left)//2 +left
            if arr[mid]==target:
                return True
            else:
                if arr[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
        return False 
    '''
