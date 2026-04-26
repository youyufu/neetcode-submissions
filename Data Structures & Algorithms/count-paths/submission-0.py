class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for i in range(m)]
        cache[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                numpaths = 0
                if i-1 >= 0:
                    numpaths += cache[i-1][j]
                if j-1 >= 0:
                    numpaths += cache[i][j-1]
                cache[i][j] = numpaths
        return cache[m-1][n-1]