class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[[1]]
        for i in range (1 ,numRows):
            arr=[1]
            for j in range (1,i):
                arr.append(pascal[i-1][j-1]+pascal[i-1][j])
            arr.append(1)
            pascal.append(arr)

        return pascal

        
