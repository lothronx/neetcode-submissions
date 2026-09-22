class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        whatever = {}
        for i, num in enumerate(nums):
            
            if target - num in whatever.keys():
                return [whatever[target - num], i]
            whatever[num] = i
            