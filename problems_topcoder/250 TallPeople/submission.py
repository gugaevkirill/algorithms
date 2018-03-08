import numpy as np


class TallPeople:
    def getPeople(self, peopleStrings):
        arr = [np.fromstring(ps, np.int16, sep=' ') for ps in peopleStrings]
        peoples = np.concatenate(arr, axis=0).reshape(len(arr), len(arr[0]))
        shortest = [np.min(group) for group in peoples]
        tallest = [np.max(group) for group in peoples.T]
        
        return (np.max(shortest), np.min(tallest))


sol = TallPeople()

# The heights 2 and 4 are the shortest from the rows, so 4 is the taller of the two.
# The heights 9, 8, and 7 are the tallest from the columns, so 7 is the shortest of the 3.
assert sol.getPeople(("9 2 3", "4 8 7")) == (4, 7)

assert sol.getPeople(("1 2", "4 5", "3 6")) == (4, 4)

# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
assert sol.getPeople(("1 1", "1 1")) == (1, 1)
