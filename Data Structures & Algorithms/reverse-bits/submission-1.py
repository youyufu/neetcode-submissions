class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            ext = (n >> i) & 1
            res += ext << (31-i)
        return res