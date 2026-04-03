class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevSum = {}
        for i, num in enumerate(nums):

            diff = target - num

            if diff in prevSum:
                return [prevSum[diff], i]
            prevSum[num] = i
        
        return []
        