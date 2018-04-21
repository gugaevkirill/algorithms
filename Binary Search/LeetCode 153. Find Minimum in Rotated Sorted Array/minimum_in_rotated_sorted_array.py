class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        >>> Solution().findMin([1])
        1
        
        >>> Solution().findMin([1, 2, 3, 4])
        1
        
        >>> Solution().findMin([4, 6, 7, 1, 2, 3])
        1
        
        >>> Solution().findMin([1, 1, 1, 1])
        1
        """
        i = 0
        j = len(nums) - 1
        while j - i > 1:
            tmp = int((j + i) / 2)
            if nums[tmp] > nums[j]:
                i = tmp
            else:
                j = tmp
        
        return min(nums[i], nums[j])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
