class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            wanted = target - num
            if wanted in seen:
                return [seen[wanted], i]
            seen[num] = i
        
        return []
        