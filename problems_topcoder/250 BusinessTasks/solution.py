import numpy as np


class BusinessTasks:
    def getTask(self, tasks: tuple, n: int) -> str:
        seed = n - 1
        todoList = list(tasks)
        
        i = 0
        while len(todoList) > 1:
            i = np.mod(i + seed, len(todoList))
            del todoList[i]
        
        return todoList[0]


solution = BusinessTasks()

# We start counting from a. So a is 1, b is 2. We remove b, so list is now {a,c,d}. We continue from c. So c is 1, d is 2. We remove d, so list is now {a,c}. We continue from a. So a is 1, c is 2. We remove c, and now we are left with the last task a.
assert solution.getTask(("a", "b", "c", "d"), 2) == 'a'

# We start counting from a. So a is 1, b is 2, c is 3. We remove c,
# now list = {a,b,d,e}. We continue from d. So d is 1, e is 2, a is 3. We remove a, now list = {b,d,e}. We continue from b. So b is 1, d is 2, e is 3. We remove e, now list = {b,d}. We continue from b. So b is 1, d is 2 and finally b is 3. We remove b, and now we are left with just one task d.
assert solution.getTask(("a", "b", "c", "d", "e"), 3) == 'd'

assert solution.getTask(("alpha", "beta", "gamma", "delta", "epsilon"), 1) == "epsilon"

assert solution.getTask(("a", "b"), 1000) == "a"

assert solution.getTask(("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                         "t", "u", "v", "w", "x", "y", "z"), 17) == "n"

# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
assert solution.getTask((
                        "zlqamum", "yjsrpybmq", "tjllfea", "fxjqzznvg", "nvhekxr", "am", "skmazcey", "piklp", "olcqvhg",
                        "dnpo", "bhcfc", "y", "h", "fj", "bjeoaxglt", "oafduixsz", "kmtbaxu", "qgcxjbfx", "my", "mlhy",
                        "bt", "bo", "q"), 9000000) == "fxjqzznvg"
