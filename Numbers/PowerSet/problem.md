# Power set
In mathematics, the power set (or powerset) of any set S is the set of all subsets of S, including the empty set and S itself.

You are to return power set of chars from string S. S and subsets of S may contain duplicate entries.

## Input format
Non-empty string

## Output format
- `Set[str]` - set of all subsets of S including `''` and `S` itself.
- Each element of result set must contain letters in lexicography sorted order.

## Examples
### Empty string
- Input: `''`
- Output: `{''}`

### Simple 1
- Input: `'a'`
- Output: `{'', 'a'}`

### Simple 2
- Input: `'cba'`
- Output: `{'', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'}`

### Duplicate letters
- Input: `'aaa'`
- Output: `{'', 'a', 'aa', 'aaa'}`

### Duplicate letters in random order
- Input: `'aba'`
- Output: `{'', 'a', 'b', 'aa', 'ab', 'aab'}`
