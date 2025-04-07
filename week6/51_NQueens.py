class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        diagl = set()
        diagr = set()
        rows = set()
        cols = set()
        checkerboard = [["."] * n for _ in range(n)]

        def backtrack(row=0):
            if row == n:
                ans.append(["".join(r) for r in checkerboard])
                return
            for col in range(n):
                if (col in cols) or ((row + col) in diagr) or ((row - col) in diagl):
                    continue
                
                checkerboard[row][col] = "Q"
                cols.add(col)
                diagr.add(row + col)
                diagl.add(row - col)

                backtrack(row + 1)

                checkerboard[row][col] = "."
                cols.remove(col)
                diagr.remove(row + col)
                diagl.remove(row - col)
        
        backtrack(0)
        return ans