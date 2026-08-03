class Solution:
    def isValid(self, s: str) -> bool:

        close_to_open = {')': '(', '}': '{', ']':'['}

        stack = []

        for char in s:

            if char not in close_to_open:
                stack.append(char)
            elif not stack or stack.pop() != close_to_open[char]:
                return False

        return not stack
        