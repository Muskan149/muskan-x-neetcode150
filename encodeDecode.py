class Solution:
    def encode(self, strs: List[str]) -> str:
        # aaabbbc,# = a#3b#2c#1,#1##1 => aaabbc,#
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1  # skip past '#'
            res.append(s[j:j+length])
            i = j + length
        return res
