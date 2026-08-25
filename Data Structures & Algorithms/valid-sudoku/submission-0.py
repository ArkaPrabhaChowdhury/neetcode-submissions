class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for val in row:
                if val == ".":
                    continue
                if val in seen or val not in "123456789":
                    return False
                seen.add(val)
        
        for j in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                val = board[i][j]
                if val == '.':
                    continue
                if val in seen or val not in "123456789":
                    return False
                seen.add(val)
                
# 3. Validate 3x3 Sub-grids (Fixed logic)
        for r in [0, 3, 6]:
            for c in [0, 3, 6]:
                seen = set()
                # Iterate through the 3x3 box starting at (r, c)
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        val = board[i][j]
                        if val == '.':
                            continue
                        if val in seen or val not in "123456789":
                            return False
                        seen.add(val)
        return True    