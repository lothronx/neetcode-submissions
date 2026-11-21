class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        widths = defaultdict(int)

        for row in wall:
            widthFromLeft = 0
            for width in row:
                widths[widthFromLeft] += 1
                widthFromLeft += width
        
        del widths[0]

        if not widths:
            return len(wall)

        return len(wall) - max(widths.values())


                
        



        