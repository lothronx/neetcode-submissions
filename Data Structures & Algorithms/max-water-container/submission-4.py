class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            res = max(res, width*height)

            if heights[l] < heights[r]:
                old_height = heights[l]
                l += 1
                while l < r and heights[l] <= old_height:
                    l += 1
            else:
                old_height = heights[r]
                r -= 1
                while l < r and heights[r] < old_height:
                    r -= 1

        return res