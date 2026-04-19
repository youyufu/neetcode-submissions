class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(heights)
        m = len(heights[0])
        pac = set()
        atl = set()

        def dfs(i, j, visit, prev_h):
            if (i, j) in visit or i < 0 or j < 0 or i >= n or j >= m or heights[i][j] < prev_h:
                return
            visit.add((i, j))
            dfs(i+1,j,visit,heights[i][j])
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
        
        for i in range(n):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, m-1, atl, heights[i][m-1])

        for j in range(m):
            dfs(0, j, pac, heights[0][j])
            dfs(n-1, j, atl, heights[n-1][j])
        
        for i in range(n):
            for j in range(m):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res