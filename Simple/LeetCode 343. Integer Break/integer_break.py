class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        
        >>> Solution().integerBreak(2)
        1
        
        >>> Solution().integerBreak(3)
        2
        
        >>> Solution().integerBreak(10)
        36
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        product = 0
        for i in range(int(n / 3) + 1):
            if (n - 3 * i) % 2 == 0:
                j = (n - 3 * i) // 2
                product = max(product, 3 ** i * 2 ** j)

        return product


if __name__ == '__main__':
    import doctest
    doctest.testmod()
