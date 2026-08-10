class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        charSet = set()

        for char in s:

            if char in charSet:
                charSet.remove(char)
            else:
                charSet.add(char)

        return not len(charSet) > len(s) % 2
            
        

