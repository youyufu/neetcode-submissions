class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                cache[j] += cache[j-1]
        
        return cache[n-1]