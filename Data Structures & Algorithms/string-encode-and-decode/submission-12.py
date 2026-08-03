class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []

        for word in strs:
            length = len(word)
            encoded_word = f"{length}#{word}"
            encoded.append(encoded_word)

        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:

        n = len(s)
        i = 0
        res = []

        while i < n:

            j = i + 1
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            j += 1
            word = s[j:j+length]
            res.append(word)
            i = j + length

        return res



