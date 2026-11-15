class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDic = {}
        res = [[] for n in range(len(nums) + 1)]
        for e in nums:
            #print(e)

            countDic[e] = countDic.get(e, 0) + 1
            res[countDic[e]].append(e)

        kMax = []
        for subset in res[::-1]:
            if subset:
                for v in subset:
                    if len(kMax) == k:
                        break

                    if v not in kMax:
                        kMax.append(v)
        return kMax