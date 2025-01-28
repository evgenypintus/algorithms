class Solution(object):


    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []

        rows = len(matrix)
        cols = len(matrix[0])

        if rows == 0:
            return res

        top = 0
        left = 0
        bottom = rows-1
        right = cols-1

        while len(res) < rows*cols:

            if top<=bottom:
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                top +=1

            if left<=right :
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right -=1

            if top<=bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -=1

            if left<=right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left +=1

            print(top, right, left, bottom)
        return res


if __name__ == '__main__':

    s = Solution()

    # matrix = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [9, 10, 11, 12]]

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]


    r = s.spiralOrder(matrix)

    print(r)