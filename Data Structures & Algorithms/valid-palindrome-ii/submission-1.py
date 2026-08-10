class Solution:
    def validPalindrome(self, s: str) -> bool:

        L, R = 0, len(s) - 1

        while L < R:

            if s[L] != s[R]:
                leftString = s[L+1: R +1]
                rightString = s[L: R]
                return leftString == leftString[::-1] or rightString == rightString[::-1]

            L, R = L + 1, R - 1

        return True
        