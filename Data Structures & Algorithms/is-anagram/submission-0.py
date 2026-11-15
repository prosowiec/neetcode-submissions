class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        if len(s) != len(t):
            return False

        for elS, elT in zip(s, t):
            if elS in dictS.keys():
                dictS[elS] +=1
            else:
                dictS[elS] = 1
            
            if elT in dictT.keys():
                dictT[elT] +=1
            else:
                dictT[elT] = 1

        for key in dictS.keys():
            if not key in dictT.keys():
                return False
            if dictS[key] != dictT[key]:
                return False

        return True