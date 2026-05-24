class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        mat = [[False for _ in range(n)] for _ in range(n)]
        count=0
        for i in range(1,n+1):
            for j in range(n-i+1):
                k=i+j-1
                if i==1:
                    mat[j][k]=True 
                elif i==2:
                    mat[j][k]=(s[j]==s[k])
                else: 
                    mat[j][k]=(s[j]==s[k]) and mat[j+1][k-1]
                if mat[j][k]:
                    count+=1
        return count

