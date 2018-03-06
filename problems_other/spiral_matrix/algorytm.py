import math


class Analytical:
    def __init__(self, d: int):
        self.d = d

    def _calculate_k(self, n: int):
        """
        k - number of full spirals started from A[0, 0] to A[0, d-1], then A[d-1, d-1], e.t.c
        
        For n is on main diagonal, n = 4((d - 1) + (d - 2) + ... + (d - k)) = 4dk - 4k(k - 1) / 2
        Therefore equation: 2 * k ** 2 - (4d - 2)k + n = 0 is right for that n
        So, k = (2d - 1) / 2 ± ((4d - 2) ** 2 - 8n) ** 0.5 / 4
        On second thoughts, k < (2d - 1) / 2, so, k = (2d - 1) / 2 - ((4d - 2) ** 2 - 8n) ** 0.5 / 4
        
        If n grows, for some time, number of full spirals, k keeps the same value, and then it raises by 1.
        Accordingly, for any n, k = math.floor((2d - 1) / 2 - ((4d - 2) ** 2 - 8n) ** 0.5 / 4)
        """
        inaccurate = (self.d - 0.5) - ((self.d - 0.5) ** 2 - n / 2) ** 0.5
        print(inaccurate)
        
        # TODO: where is the error ??
        
        return math.floor(inaccurate)


class Recursion:
    def __init__(self, d: int):
        self.d = d
    
    @staticmethod
    def _one_spiral(self, k: int, d: int):
        """
        :param k: turn number
        :param d: current edge length
        """
        
        return self._one_spiral(d)
    
    def solve(self):
        return self._one_spiral(self.d)
