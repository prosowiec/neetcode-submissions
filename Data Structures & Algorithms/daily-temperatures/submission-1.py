class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        helper_stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while helper_stack and temperatures[i] > temperatures[helper_stack[-1]]:
                j = helper_stack.pop()
                res[j] = i - j

            helper_stack.append(i)
        return res