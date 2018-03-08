Problem Statement
A group of people stand before you arranged in rows and columns. Looking from above, they form an R by C rectangle of people. You will be given a people containing the height of each person. Elements of people correspond to rows in the rectangle. Each element contains a space-delimited list of integers representing the heights of the people in that row. Your job is to return 2 specific heights in a . The first is computed by finding the shortest person in each row, and then finding the tallest person among them (the 'tallest-of-the-shortest'). The second is computed by finding the tallest person in each column, and then finding the shortest person among them (the 'shortest-of-the-tallest').
Definition
Class: TallPeople
Method: getPeople
Parameters: tuple (string)
Returns: tuple (integer)
Method signature: def getPeople(self, people):
Limits
Time limit (s): 840.000
Memory limit (MB): 64
Constraints
- people will contain between 2 and 50 elements inclusive.
- Each element of people will contain between 3 and 50 characters inclusive.
- Each element of people will be a single space-delimited list of positive integers such that:
1) Each positive integer is between 1 and 1000 inclusive with no extra leading zeros.
2) Each element contains the same number of integers.
3) Each element contains at least 2 positive integers.
4) Each element does not contain leading or trailing whitespace.
Examples
0)
{'9 2 3', '4 8 7'}
Returns: { 4, 7 }
The heights 2 and 4 are the shortest from the rows, so 4 is the taller of the two. The heights 9, 8, and 7 are the tallest from the columns, so 7 is the shortest of the 3.
1)
{'1 2', '4 5', '3 6'}
Returns: { 4, 4 }
2)
{'1 1', '1 1'}
Returns: { 1, 1 }
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.