class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
       i=0
       j=0
       length_t=len(t)
       while i < len(s) and j < length_t :
            if s[i]==t[j]:
                j+=1
            i+=1
       return length_t-j
        