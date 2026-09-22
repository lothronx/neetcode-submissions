class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            count = {}

            for c in str:
                count[c] = count.get(c, 0) + 1
            
            res[frozenset(count.items())].append(str)

        return list(res.values())