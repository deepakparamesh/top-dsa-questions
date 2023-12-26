class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnDict = collections.defaultdict(set)
        rowDict = collections.defaultdict(set)
        squareDict = collections.defaultdict(set)
        
        for row in range(9):
            for column in range(9):
                currentNum = board[row][column]
                if board[row][column] == ".":
                    continue
                
                if(
                    board[row][column] in rowDict[row] or
                    board[row][column] in columnDict[column] or
                    board[row][column] in squareDict[(row//3, column//3)]
                ):
                    return False
                
                columnDict[column].add(board[row][column])
                rowDict[row].add(board[row][column])
                squareDict[(row//3,column//3)].add(board[row][column])
        return True
