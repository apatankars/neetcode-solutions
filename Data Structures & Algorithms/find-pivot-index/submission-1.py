class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = sum(nums)


        runningSum = 0
        for idx, num in enumerate(nums):
            rightSum = total - runningSum - num
            if runningSum == rightSum:
                return idx
            runningSum += num
        
        return -1
            

        