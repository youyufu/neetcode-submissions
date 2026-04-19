class Solution:
    def countSubstrings(self, s: str) -> int:
        count_pal = 0
        def countP(l, r) -> int:
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        for i in range(len(s)):
            count_pal += countP(i, i)
            count_pal += countP(i, i+1)
        return count_pal