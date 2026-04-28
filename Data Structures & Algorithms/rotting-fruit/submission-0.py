class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        numFresh = 0
        time = 0

        # count num fresh oranges, add rotten oranges to queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    numFresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        while numFresh > 0 and queue:
            length = len(queue) # we want to do one level before increasing time
            for i in range(length):
                x, y = queue.popleft()
                for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    coordx, coordy = x + r, y + c
                    if (0 <= coordx < len(grid)) and (0 <= coordy < len(grid[0])) and grid[coordx][coordy] == 1:
                        grid[coordx][coordy] = 2
                        queue.append((coordx, coordy))
                        numFresh -= 1
            time += 1
        return time if numFresh == 0 else -1