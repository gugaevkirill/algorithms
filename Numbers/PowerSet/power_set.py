#!/usr/bin/python3
from typing import Set
from collections import Counter


def power_set_ranger(target: str) -> Set[str]:
    """
    >>> power_set_ranger('')
    ['']
    
    # Simple 1
    >>> power_set_ranger('a')
    ['', 'a']
    
    # Simple 2
    >>> power_set_ranger('cba')
    ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
    
    # Duplicate letters
    >>> power_set_ranger('aaa')
    ['', 'a', 'aa', 'aaa']
    
    # Duplicate letters in random order
    >>> power_set_ranger('aba')
    ['', 'a', 'aa', 'b', 'ab', 'aab']
    """

    letter_counts = Counter(target)
    letter_counts_sorted = sorted(letter_counts.items())
    
    power_set = ['']
    for l, count_l in letter_counts_sorted:
        power_set += [
            prefix + l * i
            for i in range(1, count_l + 1)
            for prefix in power_set
        ]

    return power_set


if __name__ == "__main__":
    import doctest
    doctest.testmod()
