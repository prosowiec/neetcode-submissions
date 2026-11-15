class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDic = {}
        res = list()
        for e in nums:
            countDic[e] = countDic.get(e, 0) + 1

        return list(sorted(countDic.keys(), key=lambda item: countDic[item]))[-k:]