class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s={}
        dic_t={}
        for char_s,char_t in zip(s,t):
            if (char_s in dic_s and dic_s[char_s]!=char_t) or (char_t in dic_t and dic_t[char_t]!=char_s):
                return False
            else:
                dic_t[char_t]=char_s
                dic_s[char_s]=char_t
        
        return True
            
