class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 1001 0101 -> 1110
        mask = 0xFFFFFFFF
        carry = 0
        res = 0

        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            curbit = abit ^ bbit ^ carry
            if curbit:
                res = res | (1 << i)
            carry = (abit & bbit) | (abit & carry) | (bbit & carry)
        
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        
        return res
