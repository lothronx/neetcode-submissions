class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixsum = defaultdict(int)
        currsum = 0

        for num in nums:
            prefixsum[currsum] += 1
            currsum += num
            res += prefixsum[currsum - k]

        return res




        