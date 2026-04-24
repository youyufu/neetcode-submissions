class Solution:
    def hammingWeight(self, n: int) -> int:
        num1 = 0
        for i in range(32):
            if (n >> i) & 1:
                num1 +=1
        return num1
