class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for num, v in count.items():
            freq[v].append(num)
        
        orderedFreq = freq[::-1]
        res = []
        for i in range(len(orderedFreq)):
            for num in orderedFreq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        