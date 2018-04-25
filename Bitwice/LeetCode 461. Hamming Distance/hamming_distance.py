import math


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        
        >>> Solution().hammingDistance(1, 4)
        2
        
        >>> Solution().hammingDistance(77, 77)
        0
        
        >>> Solution().hammingDistance(0, 0)
        0
        """

        positions = x ^ y
        if positions == 0:
            return 0
        
        count = 0
        for i in range(int(math.log(positions, 2)) + 1):
            if positions & (1 << i) != 0:
                count += 1

        return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
