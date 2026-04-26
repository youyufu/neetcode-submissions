class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)

        cache = [[0] * (l2+1) for i in range(l1+1)]
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    cache[i][j] = cache[i-1][j-1] + 1
                else:
                    cache[i][j] = max(cache[i-1][j], cache[i][j-1])
        return cache[l1][l2]
                