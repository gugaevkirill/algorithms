class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        >>> Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
        35
        
        >>> Solution().maxIncreaseKeepingSkyline([[1]])
        0
        """
        
        max_by_row = [max(row) for row in grid]
        max_by_col = [max([row[i] for row in grid]) for i in range(len(grid[0]))]
        
        hight = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                hight += min(max_by_row[i], max_by_col[j]) - grid[i][j]
        
        return hight


if __name__ == '__main__':
    import doctest
    doctest.testmod()