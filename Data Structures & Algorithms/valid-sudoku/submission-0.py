class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def hasDuplicate(numbers: List[str]):
            visited = [False]*10
            for num in numbers:
                if num == ".":
                    continue
                if visited[int(num)] == True:
                    return True
                visited[int(num)] = True
            return False
                
        #rows
        for row in board:
            if hasDuplicate(row):
                return False
        
        # columns
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if hasDuplicate(column):
                return False
        # boxes
        for l in range(3):
            for i in range(3):
                box = []
                for j in range(3):
                    for k in range(3):
                        box.append(board[j+3*l][k+3*i])
                if hasDuplicate(box):
                    return False

        return True
        