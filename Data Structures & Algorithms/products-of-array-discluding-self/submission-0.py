class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        preProd = [1] * (n+1)
        postProd = [1] * (n+1)

        for i in range(len(nums)):
            preProd[i+1] = preProd[i] * nums[i]

        for i in range(n - 1, -1, -1):
            postProd[i] = postProd[i+1] * nums[i]

        res = []
        for i in range(n):
            res.append(preProd[i] * postProd[i+1])

        return res


        