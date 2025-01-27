from copy import deepcopy

class Solution(object):

    def out_of_bound(self, row, column, height, width):

        if row<0 or column<0 or row == height or column == width:
            return True
        return False

    def get_neighbours(self, row, column, state_board):

        count = 0
        height = len(state_board)
        width = len(state_board[0])
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if not self.out_of_bound(row+i, column+j, height, width) and not (i==0 and j==0):

                    count += state_board[row+i][column+j]
        return count

    def cell_state(self, row, column, state_board):

        n = self.get_neighbours(row, column, state_board)

        # live cell
        if state_board[row][column] == 1:
            if n < 2 or n > 3:
                return 0
        else:
            if n == 3:
                return 1

        return state_board[row][column]


    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        state_board = deepcopy(board)
        height = len(state_board)
        width = len(state_board[0])

        for row in range(height):
            for column in range(width):
                board[row][column] = self.cell_state(row, column, state_board)

if __name__ == '__main__':

    s = Solution()

    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

    s.gameOfLife(board)

    print(board)