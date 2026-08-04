class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        seenStack = []
        maxArea = 0
        n = len(heights)

        for idx, height in enumerate(heights):
            startIdx = idx
            while seenStack and height < seenStack[-1][0]:
                prevHeight, prevIdx = seenStack.pop()
                currArea = prevHeight * (idx - prevIdx)
                maxArea = max(maxArea, currArea)
                startIdx = prevIdx

            seenStack.append((height, startIdx))

        while seenStack:
                prevHeight, prevIdx = seenStack.pop()
                currArea = prevHeight * (n - prevIdx)
                maxArea = max(maxArea, currArea)

        return maxArea
