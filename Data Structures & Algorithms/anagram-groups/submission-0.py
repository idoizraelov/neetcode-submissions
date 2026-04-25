class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            temp=tuple(count)
            if temp in dic:
                dic[temp].append(s)
            else:
                dic[temp]=[s]
        return list(dic.values())