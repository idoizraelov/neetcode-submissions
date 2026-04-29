class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_card=sum(cardPoints[:k])
        max_point=0
        i=k-1
        j=len(cardPoints)-1
        while j>=len(cardPoints)-k-1:
            max_point=max(sum_card,max_point)
            print(i,j)
            sum_card+=(cardPoints[j]-cardPoints[i])
            i-=1
            j-=1

        return max_point