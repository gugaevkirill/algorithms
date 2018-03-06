Problem Statement
A busy businessman has a number of equally important tasks which he must accomplish. To decide which of the tasks to perform first, he performs the following operation.

He writes down all his tasks in the form of a circular list, so the first task is adjacent to the last task. He then thinks of a positive number. This number is the random seed, which he calls n. Starting with the first task, he moves clockwise (from element 1 in the list to element 2 in the list and so on), counting from 1 to n. When his count reaches n, he removes that task from the list and starts counting from the next available task. He repeats this procedure until one task remains. It is this last task that he chooses to execute.

Given a list representing the tasks and an n, return the task which the businessman chooses to execute.

Definition
Class: BusinessTasks
Method: getTask
Parameters: tuple (string), integer
Returns: string
Method signature: def getTask(self, list, n):
Limits
Time limit (s): 840.000
Memory limit (MB): 64
Constraints
- list will contain between 2 and 50 elements inclusive.
- Each element in list will contain between 1 and 50 characters inclusive.
- Each element in list will contain only characters 'a'-'z'.
- n will be between 1 and 10000000 inclusive.
Examples
0)
{"a","b","c","d"}
2
Returns: "a"
We start counting from a. So a is 1, b is 2. We remove b, so list is now {a,c,d}. We continue from c. So c is 1, d is 2. We remove d, so list is now {a,c}. We continue from a. So a is 1, c is 2. We remove c, and now we are left with the last task a.
1)
{"a","b","c","d","e"}
3
Returns: "d"
We start counting from a. So a is 1, b is 2, c is 3. We remove c, now list = {a,b,d,e}. We continue from d. So d is 1, e is 2, a is 3. We remove a, now list = {b,d,e}. We continue from b. So b is 1, d is 2, e is 3. We remove e, now list = {b,d}. We continue from b. So b is 1, d is 2 and finally b is 3. We remove b, and now we are left with just one task d.
2)
{"alpha","beta","gamma","delta","epsilon"}
1
Returns: "epsilon"
3)
{"a","b"}
1000
Returns: "a"
4)
{"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t", "u","v","w","x","y","z"}
17
Returns: "n"
5)
{"zlqamum","yjsrpybmq","tjllfea","fxjqzznvg","nvhekxr","am","skmazcey","piklp", "olcqvhg","dnpo","bhcfc","y","h","fj","bjeoaxglt","oafduixsz","kmtbaxu", "qgcxjbfx","my","mlhy","bt","bo","q"}
9000000
Returns: "fxjqzznvg"
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.