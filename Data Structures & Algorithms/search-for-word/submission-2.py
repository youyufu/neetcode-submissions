class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        seen = set()
        def dfs(i, j, ind):
            if ind == len(word):
                return True
            if (i, j) in seen:
                return False
            if not (0 <= i < m) or not (0 <= j < n) or board[i][j] != word[ind]:
                return False
            seen.add((i, j))
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if dfs(i+x,j+y,ind+1):
                    return True
            seen.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False