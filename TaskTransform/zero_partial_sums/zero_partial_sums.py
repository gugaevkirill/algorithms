from typing import List
import time
from collections import defaultdict


class ZeroSumsCounter:
    def zero_sums(self, mas: List[float]) -> int:
        start_time = time.time()

        sums = defaultdict(int)
        current_sum = 0
        count = 0
        
        for el in mas:
            current_sum += el
            count += sums[current_sum]
            if current_sum == 0:
                count += 1

            sums[current_sum] += 1

        eval_time = round(time.time() - start_time, 4)
        print(f'{eval_time} sec', end='\n\n')
        
        return count


solver = ZeroSumsCounter()

# 0 sum
assert 0 == solver.zero_sums([])

# 0 sum #2
assert 0 == solver.zero_sums([1, 2, 3, 4, 5])

# 1 sum
assert 1 == solver.zero_sums([0])

# 2 sum
# Explanation: sum from `0` index to `2` & `1'st` el.
assert 2 == solver.zero_sums([1, 0, -1])

# 4 sum
# Explanation: `(1, 1), (0, 2), (1, 3), (2, 3)`
assert 4 == solver.zero_sums([1, 0, -1, 1, 6])
