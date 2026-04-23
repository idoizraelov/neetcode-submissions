class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        monim= [0]*26
        for c in s:
            monim[ord(c)-ord('a')]+=1       
        for c in t:
            if  monim[ord(c)-ord('a')]==0 :
                return False 
            monim[ord(c)-ord('a')]-=1
        
        return True 
