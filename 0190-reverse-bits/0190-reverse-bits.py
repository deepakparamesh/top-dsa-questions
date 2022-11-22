class Solution:
    def reverseBits(self, n: int) -> int:

        # reverse all the bits that is given
        
        # convert the reversed bits into integer

        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        return res

