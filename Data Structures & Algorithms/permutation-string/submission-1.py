class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        wordCount = {}
        for e in s1:
            wordCount[e] = wordCount.get(e, 0) + 1

        needed = len(wordCount)
        for r in range(len(s2)):
            wordCounts2, cur = {}, 0
            for i in range(r, len(s2)):
                wordCounts2[s2[i]] = wordCounts2.get(s2[i], 0) + 1
                if wordCounts2[s2[i]] > wordCount.get(s2[i], 0):
                    break
                if wordCounts2[s2[i]] == wordCount[s2[i]]:
                    cur +=1
                
                if cur == needed:
                    return True



        return False            