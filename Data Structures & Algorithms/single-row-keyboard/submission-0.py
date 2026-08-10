class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        charToIdx = {}

        for idx, char in enumerate(keyboard):

            charToIdx[char] = idx

        res = 0
        prevPos = 0
        for char in word:
            newPos = charToIdx[char]
            res += abs(prevPos - newPos)
            prevPos = newPos
        
        return res

        