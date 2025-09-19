class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if not s:
            return ""
        if not order:
            return s
        
        char_freq = Counter(s)

        result = []

        for char in order:
            if char in char_freq:
                count = char_freq[char]
                result.extend([char] * count)

                del char_freq[char]

        for char, count in char_freq.items():
            result.extend([char] * count)

        return ''.join(result)


        # order = "bcafg", s = "abcd"

        # {a:1,b:1,c:1,d:1}

        # result =  b
        # result =  bc
        # result =  bca



