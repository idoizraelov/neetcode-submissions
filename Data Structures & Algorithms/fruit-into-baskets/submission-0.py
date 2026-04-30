class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_window=0
        l=0
        dic={}
        for r in range(len(fruits)):
            if len(dic)<=2:
                if fruits[r] in dic:
                    dic[fruits[r]]+=1
                else:
                    dic[fruits[r]]=1
            while len(dic)>2:
                dic[fruits[l]]-=1
                if dic[fruits[l]]==0:
                    dic.pop(fruits[l])
                l+=1
            max_window=max(max_window,r-l+1)
            
        return max_window