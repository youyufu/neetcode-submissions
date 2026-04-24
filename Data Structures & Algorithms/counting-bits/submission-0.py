class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            num1 = 0
            while i != 0:
                i = i & (i-1)
                num1 += 1
            res.append(num1)
        return res