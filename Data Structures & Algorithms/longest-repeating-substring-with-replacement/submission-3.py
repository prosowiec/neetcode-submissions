class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wordCount = {}
        l = 0
        max_size = 0
        maxf = 0
        replaced_count = 0
        for r in range(len(s)):
            wordCount[s[r]] = wordCount.get(s[r], 0) + 1
            maxf = max(wordCount.get(s[r]), maxf)

            while maxf + k < r - l + 1:
                wordCount[s[l]] -=  1
                l+=1
            
            max_size = max(max_size, r - l + 1)

        return max_size

