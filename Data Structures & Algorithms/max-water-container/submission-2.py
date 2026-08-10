class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0

        L, R = 0, len(heights) - 1

        while L < R:

            leftHeight = heights[L]
            rightHeight = heights[R]

            currArea = min(leftHeight, rightHeight) * (R - L)
            maxArea = max(maxArea, currArea)

            if leftHeight < rightHeight:
                L += 1
            else:
                R -= 1
        
        return maxArea