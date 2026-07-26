class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # first, we map each number to its count

        # then we can create an array (size n + 1)

        # iterate backwards, popping until we pop k elems

        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for num, count in counter.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, -1, -1):

            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


        