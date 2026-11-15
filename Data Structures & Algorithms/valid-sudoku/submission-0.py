class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnCheck = [set() for _ in range(9)]
        boxCheck = [set() for _ in range(9)]

        for i, row in enumerate(board):
            rowCheck = set()
            addedColCheck = False
            for j, col in enumerate(row):
                if i % 3 == 1 and j % 3 == 1:

                    edgesInBox = set()
                    for box_i in range(i - 1, i + 2):
                        for box_j in range(j - 1, j + 2):
                            if board[box_i][box_j] == ".":
                                continue
                            if board[box_i][box_j] in edgesInBox:
                                return False
                            edgesInBox.add(board[box_i][box_j])

                if col == '.':
                    continue
                
                col = int(col)
                if col < 1 and col > 9:
                    return False

                if col in rowCheck:
                    return False
                rowCheck.add(col)

                if col in columnCheck[j]:
                    return False
                columnCheck[j].add(col)
                
                #boxNumber = (i + j + 2) 

                #print(boxNumber)

        return True