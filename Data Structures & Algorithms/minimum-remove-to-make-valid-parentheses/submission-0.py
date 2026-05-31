class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left=[]
        count=0
        for c in s:
            if c=="(":
                left.append(c)
                count+=1
            elif c==")" and count>0:
                left.append(c)
                count-=1
            elif c!=")":
                left.append(c)
        res=[]
        for c in reversed(left):
            if c == "(" and count>0:
                count-=1
            else:
                res.append(c)
    
        return "".join(reversed(res))
