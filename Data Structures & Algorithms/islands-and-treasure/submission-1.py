class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for offx, offy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    x, y = r + offx, c + offy
                    if min(x, y) < 0 or x == m or y == n or grid[x][y] == -1 or (x, y) in visited:
                        continue
                    q.append([x, y])
                    visited.add((x, y))
            dist += 1
