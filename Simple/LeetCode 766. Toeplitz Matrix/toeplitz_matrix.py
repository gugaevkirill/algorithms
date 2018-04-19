class Solution:

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        
        # Example 1
        >>> Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
        True
        
        # Example 2
        >>> Solution().isToeplitzMatrix([[1,2],[2,2]])
        False
        """
        
        if not matrix:
            return True
        
        m = len(matrix)
        n = len(matrix[0])
        
        """
        1234
        5123
        9512
        """
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
