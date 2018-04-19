class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        
        >>> solver = Solution()
        >>> solver.validPalindrome('aba')
        True
        
        >>> solver.validPalindrome('abca')
        True
        
        >>> solver.validPalindrome('12334421')
        False
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.check_palindrome(s, i + 1, j) or self.check_palindrome(s, i, j - 1)
            i += 1
            j -= 1

        return True

    @staticmethod
    def check_palindrome(s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
