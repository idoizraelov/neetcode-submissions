class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_char=Counter(chars)
        count=0
        for word in words:
            count_word=Counter(word)
            if count_word<=count_char:
                count+=len(word)

        return count