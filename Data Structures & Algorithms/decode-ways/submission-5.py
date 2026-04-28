class Solution:
    def numDecodings(self, s: str) -> int:
        dp2 = 0
        dp1 = 1
        new = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                new = 0
            else:
                new = dp1
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and (s[i + 1] in "0123456"))):
                new += dp2
            new, dp1, dp2 = 0, new, dp1
        return dp1