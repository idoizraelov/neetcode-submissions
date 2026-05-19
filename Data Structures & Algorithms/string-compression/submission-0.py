class Solution:
    def compress(self, chars: List[str]) -> int:
        i,k=0,0
        while i<len(chars):
            j=i
            while j<len(chars) and chars[i]==chars[j]:
                j+=1
            chars[k]=chars[i]
            k+=1
            count=j-i
            if count>1:
                for dig in str(count):
                    chars[k]=dig
                    k+=1
            i=j

        return k

