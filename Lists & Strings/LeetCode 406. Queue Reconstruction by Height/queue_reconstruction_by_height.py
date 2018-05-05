class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        
        >>> Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        
        >>> Solution().reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]])
        [[3, 0], [6, 0], [7, 0], [5, 2], [3, 4], [5, 3], [6, 2], [2, 7], [9, 0], [1, 9]]
        """
        people.sort(key=lambda x: [x[0], -x[1]], reverse=True)
        qres = []
        for men in people:
            qres.insert(men[1], men)
        
        return qres


if __name__ == '__main__':
    import doctest
    doctest.testmod()
