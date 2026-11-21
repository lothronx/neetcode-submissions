class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowSeen = defaultdict(set)
        colSeen = defaultdict(set)
        boxSeen = defaultdict(set)

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                
                if curr in rowSeen[i]:
                    return False
                rowSeen[i].add(curr)

                if curr in colSeen[j]:
                    return False
                colSeen[j].add(curr)

                boxNumber = (i // 3, j // 3)
                
                if curr in boxSeen[boxNumber]:
                    return False
                boxSeen[boxNumber].add(curr)

                
        return True

        