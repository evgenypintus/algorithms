class Solution(object):

    visited = set()

    def dfs(self, i, j, grid):

        if (i,j) in  self.visited:
            return

        # if we reach water by any means either beyond bounds or zero cell - return
        if i < 0 or j < 0 or i >= len(grid) or j >=len(grid[0]) or grid[i][j] == '0':
            return

        # Mark cell as visited
        self.visited.add((i,j))

        # traverse all neighbour cells
        for k, l in ((-1,0), (1,0), (0, 1), (0, -1)):
                self.dfs(i+k, j+l, grid)


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        islands = 0
        self.visited.clear()

        # Search through all grid
        for i in range(m):
            for j in range(n):
                # if we find a new island count it and traverse all connected land
                if grid[i][j] != '0' and (i,j) not in self.visited:
                    islands += 1
                    self.dfs(i,j, grid)

        return islands

if __name__ == '__main__':

    s = Solution()
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
    n = s.numIslands(grid)
    assert n == 1

    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    n = s.numIslands(grid)
    assert n == 3
