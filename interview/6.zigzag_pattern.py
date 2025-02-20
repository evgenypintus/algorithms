class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result_matrix = []
        result = ''
        n = len(s)
        i = 0
        row = 0
        while i < n:

            # Read direct path
            result_matrix.append([''] * numRows)
            k=0
            while i < n and k < numRows:
                result_matrix[row][:k] = s[i]
                k += 1
                i += 1

            row +=1

            # Read zigzag
            l = 1
            while i < n and l < numRows-1:
                result_matrix.append([])
                row_list = [''] * numRows
                row_list[-1-l] = s[i]
                result_matrix[row] = row_list
                i += 1
                l += 1
                row +=1

        for j in range(numRows):
            for i in range(len(result_matrix)):
                result += result_matrix[i][j]
        return result

if __name__ == '__main__':
    s = Solution()

    string = "PAYPALISHIRING"
    numRows = 4

    print(s.convert(string, numRows))
