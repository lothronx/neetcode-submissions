class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            s1 = str(len(s)) + "#" + s
            encoded_string += s1

        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1 + length
            decoded_strs.append(s[j + 1:i])
            
        return decoded_strs;
