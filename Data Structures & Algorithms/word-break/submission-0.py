class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check=[False]*(len(s)+1)
        check[0]=True
        for i in range(len(s)):
            if check[i]==True:
                for w in wordDict:
                    if i+len(w)<=len(s) and s[i]==w[0] and s[i:i+len(w)]==w:
                        check[i+len(w)]=True
                
                        
        return check[len(s)]
                    
                    