from typing import Set
from collections import defaultdict, OrderedDict


def power_set_ranger(target: str) -> Set[str]:
    letter_counts = defaultdict(int)
    for l in target:
        letter_counts[l] += 1
    
    letter_counts_sorted = OrderedDict(sorted(letter_counts.items()))
    
    power_set = {''}
    for l, count_l in letter_counts_sorted.items():
        new_elements = set()
        for prefix in power_set:
            for i in range(1, count_l + 1):
                new_elements.add(prefix + l * i)
        power_set = power_set.union(new_elements)

    return power_set
        

# Empty string
assert {''} == power_set_ranger('')

# Simple 1
assert {'', 'a'} == power_set_ranger('a')

# Simple 2
assert {'', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'} == power_set_ranger('cba')

# Duplicate letters
assert {'', 'a', 'aa', 'aaa'} == power_set_ranger('aaa')

# Duplicate letters in random order
assert {'', 'a', 'b', 'aa', 'ab', 'aab'} == power_set_ranger('aba')
