class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        
        >>> Solution().shortestToChar('loveleetcode', 'e')
        [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        
        >>> Solution().shortestToChar('eee', 'e')
        [0, 0, 0]
        """
        
        i = S.find(C)
        indexes = []
        while i >= 0:
            indexes.append(i)
            i = S.find(C, i + 1)
        
        # left start
        distances = list(range(indexes[0], -1, -1))
        
        prev = indexes[0]
        for curr in indexes[1:]:
            middle = (curr - prev) / 2.0
            distances += list(range(1, int(middle) + 1))
            distances += list(range(int(middle - 0.5), -1, -1))
            prev = curr
        
        # right finish
        distances += list(range(1, len(S) - len(distances) + 1))
        
        return distances


if __name__ == '__main__':
    import doctest
    doctest.testmod()
