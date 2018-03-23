import time

import numpy as np


class Backpack:

    def max_items(self, capacity: int, weights: tuple, values: tuple) -> float:
        '''
        Dynamic by weight & count of items:
        1) We will calculate A[w, i], w - max possible weight, max index of possible items (we can pick from 0 to i)
        2) Recurrent formula: A[w, i + 1] = max(A[w, i], A[w - weights[i], i] + values[i])
        3) Start points: A[w, 0] = values[0] if w > weights or 0
        4) We will start from A[0, 0] to A[0, num_items], than start from A[1, 0] to A[1, num_items], e. t. c
        5) Answer = A[capacity, num_items]
        '''
        
        start_time = time.time()
        
        num_items = len(weights)
        a = np.zeros((capacity + 1, num_items), dtype=np.float)
        
        for w in range(1, capacity + 1):
            for i in range(num_items):
                a[w, i] = self._calc_a(a, w, i, weights, values)
                print(a[w, i], end='  ', flush=True)
            print('\n')
        
        eval_time = round(time.time() - start_time, 4)
        print(f'{eval_time} sec', end='\n\n')
        
        return a[capacity, num_items - 1]
    
    def _calc_a(self, a, w: int, i: int, weights: tuple, values: tuple):
        if i == 0:
            return values[i] if w >= weights[i] else 0
        
        without_i = a[w, i - 1]
        
        if w < weights[i]:
            return without_i
        
        with_i = a[w - weights[i], i - 1] + values[i]
        
        return np.max([with_i, without_i])


backpack = Backpack()

# Tests:
#### All items:
assert 6.0 == backpack.max_items(10, (1, 2, 3), (2, 2, 2))

#### Max valuable item
assert 25.0 == backpack.max_items(8, (2, 2, 2, 2, 7), (1, 1, 2, 1, 25))

#### Not so obvious set
assert 10.0 == backpack.max_items(6, (4, 3, 3), (8, 5, 5))

#### Full backpack
assert 8.0 == backpack.max_items(8, (1, 1, 2, 2, 3), (1, 1, 2, 2, 3))
