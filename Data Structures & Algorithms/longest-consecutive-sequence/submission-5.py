class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in seen:
            if num - 1 in seen:
                continue
             
            start = num
            count = 1
            while start + 1 in seen:
                count += 1
                start += 1
            res = max(res, count)
        return res
             

        