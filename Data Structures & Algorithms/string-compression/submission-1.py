class Solution:
    def compress(self, chars: List[str]) -> int:

        numConsec = 0
        prevChar = chars[0]
        reWrite = 0

        for i in range(len(chars)):

            if chars[i] == prevChar:
                numConsec += 1
            else:
                chars[reWrite] = prevChar
                reWrite += 1
                if numConsec > 1:
                    for char in str(numConsec):
                        chars[reWrite] = char
                        reWrite += 1
                prevChar = chars[i]
                numConsec = 1
        
        chars[reWrite] = prevChar
        reWrite += 1
        if numConsec > 1:
            for char in str(numConsec):
                chars[reWrite] = char
                reWrite += 1

        return reWrite