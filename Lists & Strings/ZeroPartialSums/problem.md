# Zero partial sums
Given the array of floats. You are to find number of all partial sums, equals to 0.

## Definition
- Class: `ZeroSumsCounter`
- Method: `zero_sums`
- Parameters: `List[float]`
- Returns: `int`, number of zero partial sums
- Method signature: def zero_sums(self, mas):

## Limits
- Computation limit: `O(n)`

## Examples

### 0 sum
Input: `[]`
Output: `0`

### 0 sum #2
Input: `[1, 2, 3, 4, 5]`
Output: `0`

### 1 sum
Input: `[0]`
Output: `1`

### 2 sum
Input: `[1, 0, -1]`
Output: `2`
Explanation: sum from `0` index to `2` & `1'st` el.

### 4 sum
Input: `[1, 0, -1, 1, 6]`
Output: `4`
Explanation: `(1, 1), (0, 2), (1, 3), (2, 3)`