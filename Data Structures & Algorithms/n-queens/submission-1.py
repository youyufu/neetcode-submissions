class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]

        # Not safe positions
        col = set()
        diagLeft = set()
        diagRight = set()

        def backtrack(r):
            if r == n:
                sol = ["".join(row) for row in board]
                res.append(sol)
                return
            
            # Try placing queen
            for c in range(n):
                # check if safe
                if c in col or (r+c) in diagLeft or (r-c) in diagRight:
                    continue
                # add positions to sets
                col.add(c)
                diagLeft.add(r+c)
                diagRight.add(r-c)
                board[r][c] = "Q"
                backtrack(r + 1)
                # undo changes
                col.remove(c)
                diagLeft.remove(r+c)
                diagRight.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return res