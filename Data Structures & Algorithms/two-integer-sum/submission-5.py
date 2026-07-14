class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffToIdx = {}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in diffToIdx:
                return [diffToIdx[diff], idx]
            diffToIdx[num] = idx



        