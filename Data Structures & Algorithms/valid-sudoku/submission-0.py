from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowSets = defaultdict(set)
        colSets = defaultdict(set)
        gridSets = defaultdict(set)

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            gridRow = row // 3
            for col in range(cols):
                gridCol = col // 3
                val = board[row][col]

                if val != '.':

                    if val in rowSets[row] or val in colSets[col] or val in gridSets[(gridRow, gridCol)]:
                        return False
                    rowSets[row].add(val)
                    colSets[col].add(val)
                    gridSets[((gridRow, gridCol))].add(val)

        return True
        