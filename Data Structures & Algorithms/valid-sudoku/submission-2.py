class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        sqr = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                mask = 1 << (int(board[i][j]) - 1)
                if mask & row[i] or mask & col[j] or mask & sqr[(i // 3) * 3 + (j // 3)]:
                    return False

                row[i] |= mask
                col[j] |= mask
                sqr[(i // 3) * 3 + (j // 3)] |= mask

        return True
