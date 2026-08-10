class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        sPointer = tPointer = 0

        while sPointer < len(s):

            if tPointer != len(t) and s[sPointer] == t[tPointer]:
                tPointer += 1
            sPointer += 1

        return len(t[tPointer:])

        