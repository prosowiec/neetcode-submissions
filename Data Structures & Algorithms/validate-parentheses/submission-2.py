class Solution:
    def isValid(self, s: str) -> bool:
        checkDick = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        seen = []
        for e in s:
            if e in checkDick.keys() and len(seen) == 0:
                return False
            elif e in checkDick.keys():
                pop_top = seen.pop()
                if checkDick[e] != pop_top:
                    return False
            else:
                seen.append(e)

        return len(seen) == 0