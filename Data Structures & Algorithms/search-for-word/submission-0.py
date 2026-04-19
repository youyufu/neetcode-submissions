class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (not (0 <= r <= len(board)-1)) or (not (0 <= c <= len(board[0])-1)):
                return False
            if (r, c) in path or board[r][c] != word[i]:
                return False
            path.add((r, c))
            found = dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1)
            if not found:
                path.remove((r, c))
                return False
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                found = dfs(i, j, 0)
                if found:
                    return found
        return False    