class Solution(object):

    rows = dict()
    columns = dict()
    boxes = dict()

    def get_box(self, row, column):
        return (int(column/3)+1) + int(row/3)*3

    def check_row(self, row, value):

        if row in self.rows:
            if value in self.rows[row]:
                return False
            self.rows[row].add(value)

        else:
            self.rows[row] = set()
            self.rows[row].add(value)
        return True

    def check_column(self, column, value):

        if column in self.columns:
            if value in self.columns[column]:
                return False
            self.columns[column].add(value)
        else:
            self.columns[column] = set()
            self.columns[column].add(value)
        return True

    def check_box(self, row, column, value):
        box = self.get_box(row, column)

        if box in self.boxes:
            if value in self.boxes[box]:
                return False
            self.boxes[box].add(value)
        else:
            self.boxes[box] = set()
            self.boxes[box].add(value)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.rows.clear()
        self.columns.clear()
        self.boxes.clear()

        for row in range(9):
            for column in range(9):
                if board[row][column] != '.':
                    if not self.check_row(row, board[row][column]):
                        return False
                    if not self.check_column(column, board[row][column]):
                        return False
                    if not self.check_box(row, column, board[row][column]):
                        return False
        return True

if __name__ == '__main__':

    s = Solution()

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    r = s.isValidSudoku(board)

    print(r)
