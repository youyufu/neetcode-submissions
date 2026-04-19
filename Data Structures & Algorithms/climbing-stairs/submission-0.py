class Solution:
    def climbStairs(self, n: int) -> int:
        prev1=1
        prev2=1
        for i in range(n+1):
            if i == 0 or i == 1:
                continue
            num = prev1 + prev2
            prev2 = prev1
            prev1 = num
        return prev1