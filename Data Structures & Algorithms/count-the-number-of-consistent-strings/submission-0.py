class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set=set(allowed)
        count=0
        for word in words:
            if set(word)<=allowed_set:
                count+=1
            
        return count
            
            