class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for element in strs:
            encoded =  encoded + str(len(element)) + "|" + element

        return  encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        res = []
        curIndex = 0

        while curIndex < len(s):
            delimiterIndex = s[curIndex:].find("|") + curIndex
            print(curIndex, delimiterIndex, s[curIndex:delimiterIndex])
            wordNumber = int(s[curIndex:delimiterIndex])
            delimiterIndex+=1
            codedString = s[delimiterIndex: delimiterIndex + wordNumber]
            decoded.append(codedString)
            
            curIndex = wordNumber + delimiterIndex

        return decoded