class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        sub=[]
        for i,s1 in enumerate(words):
            for s2 in words[i+1:]:
                if s1 in s2:
                    sub.append(s1)
                    break
        return sub
