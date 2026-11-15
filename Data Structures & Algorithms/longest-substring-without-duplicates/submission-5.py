class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hSet = []
        help_set = set()
        max_size = 0

        for e in s:

            if e not in help_set:
                hSet.append(e)
                help_set.add(e)
                max_size = max(max_size, len(hSet))
            else:
                while e in help_set:
                    help_set.remove(hSet.pop(0))

                help_set.add(e)
                hSet.append(e)

        return max_size