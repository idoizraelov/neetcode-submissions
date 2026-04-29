class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxium=0
        window=set()
        i,j=0,0
        while j<len(s):
            while s[j] in window:
                window.remove(s[i])
                i+=1
            window.add(s[j])
            j+=1
            maxium=max(maxium,j-i)

        return maxium
                