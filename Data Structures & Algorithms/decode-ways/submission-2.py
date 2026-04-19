class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        past1 = 1
        past2 = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                res = 0
            else:
                res = past1
            
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += past2
            
            res, past1, past2 = 0, res, past1
        
        return past1
