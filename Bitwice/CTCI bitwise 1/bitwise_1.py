def solve(m: int, n: int, i: int, j: int):
    """
    >>> solve(3, 85, 2, 4)
    77
    
    >>> solve(0, 7, 0, 0)
    6
    
    >>> solve(7, 0, 1, 4)
    14
    """
    if 2**(j - i + 1) <= m:
        raise ValueError
    
    mask = ~((2 ** (j - i + 1) - 1) << i)
    num = n & mask
    num |= m << i
    
    return num


if __name__ == '__main__':
    import doctest
    doctest.testmod()
