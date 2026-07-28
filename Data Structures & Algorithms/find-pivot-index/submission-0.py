class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        postSum = [0] * (n+1)

        for i in range(n - 1, -1, -1):
            postSum[i] = postSum[i+1] + nums[i]

        total = 0

        for idx, num in enumerate(nums):
            if total == postSum[idx+1]:
                return idx
            total += num
        
        return -1
        