class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        char_count = {char: 0 for char in order}

        for char in s:
            if char in char_count:
                char_count[char] += 1
        
        for char in order:
            res += char * char_count[char]
        
        for char in s:
            if char not in char_count:
                res += char
        
        return res

        

        