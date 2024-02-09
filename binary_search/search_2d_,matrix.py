"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = self.search_row(matrix, target)
        if row != -1:
            # We don't need to search a value
            if target in matrix[row]:
                return True
        return False

    def search_row(self, matrix, target, up=0, bottom=None):

        if bottom is None:
            bottom = len(matrix)-1

        mid = (up+bottom) // 2

        if up <= bottom:
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return mid
            # target upper mid
            if matrix[mid][0] > target:
                return self.search_row(matrix, target, up, mid-1)
            else:
                return self.search_row(matrix, target, mid+1, bottom)
        else:
            return -1


    def search_bi(self, row, target, left=0, right=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if right is None:
            right = len(row)-1

        mid = (left+right) // 2

        if left <= right:
            if row[mid] == target:
                return True

            if row[mid] > target:
                return self.search_bi(row, target, left, mid-1)
            else:
                return self.search_bi(row, target, mid+1, right)
        else:
            return False


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

    target = 3

    s = Solution()

    print(s.searchMatrix(matrix, target))