import time


class BridgeCrossing:
    def __init__(self):
        self._times = []

    def minTime(self, times):
        """
        # The example from the text.
        >>> crossing = BridgeCrossing()
        >>> crossing.minTime((1, 2, 5, 10))
        17
        
        # One solution is: 1 and 2 cross together (2min), 1 goes back (1min), 4 and 5 cross together (5min),
        # 2 goes back (2min), 1 and 3 cross together (3min), 1 goes back (1min), 1 and 2 cross together (2min).
        # This yields a total of 2 + 1 + 5 + 2 + 3 + 1 + 2 = 16 minutes spent.
        >>> crossing.minTime((1, 2, 3, 4, 5))
        16
        
        # Only one person crosses the bridge once.
        >>> crossing.minTime((100,))
        100
        
        >>> crossing.minTime((1, 2, 3, 50, 99, 100))
        162
        """
        print(times)
        start_time = time.time()

        self._times = times
        ans = self._solve(tuple(i for i in range(len(times))), tuple())

        eval_time = round(time.time() - start_time, 4)
        print(f'{eval_time} sec', end='\n\n\n')

        return ans

    def _solve(self, left_initial, right_initial):
        """
        >>> crossing = BridgeCrossing()
        >>> crossing._times = (1, 2, 5, 10)
        >>> crossing._solve((0, 1), (2, 3))
        2
        
        >>> crossing._solve((0, 1, 2), (3,))
        8

        :param set left:
        :param set right:
        :return int:
        """

        if len(left_initial) < 3:
            return max(tuple(self._times[i] for i in left_initial))

        # Recursively find minimum
        min_time = 2 * sum(self._times)
        for i in left_initial:
            for j in left_initial:
                if i >= j:
                    continue

                right = set(right_initial)
                left = set(left_initial)

                right.add(i)
                right.add(j)
                left.remove(i)
                left.remove(j)

                fastest = self._find_fastest(right)
                right.remove(fastest)
                left.add(fastest)

                time_to_cross = max(self._times[i], self._times[j]) + self._times[fastest]
                total_time = time_to_cross + self._solve(tuple(left), tuple(right))

                if total_time < min_time:
                    min_time = total_time

        return min_time

    def _find_fastest(self, indexes):
        min = 101
        min_index = False
        for i in indexes:
            if self._times[i] < min:
                min = self._times[i]
                min_index = i

        return min_index


if __name__ == "__main__":
    import doctest
    doctest.testmod()
