# Problem Statement
NOTE: This problem statement contains images that may not display properly if viewed outside of the applet.
Given a regular square grid, with some number of squares marked, find the largest circle you can draw on the grid that does not pass through any of the marked squares. The circle must be centered on a grid point (the corner of a square) and the radius must be an integer. Return the radius of the circle.

The grid will be given as a , with each character representing a square. A '.' represents an empty square, and a '#' represents a marked square.

The circle may intersect the corner of a marked square, but may not pass through the interior. For example, given the grid:


  { "############",
    "###......###",
    "##.######.##",
    "#.########.#",
    "#.##..####.#",
    "#.##..####.#",
    "#.########.#",
    "#.########.#",
    "#.########.#",
    "##.######.##",
    "###......###",
    "############" }
two circles can be drawn with radii 1 and 5, as shown below:


Therefore, your method should return 5.

Circles may not extend outside of the grid, and must have a radius of at least 1. If no such circle exists, return 0.

## Definition
- Class: LargestCircle
- Method: radius
- Parameters: tuple (string)
- Returns: integer
- Method signature: def radius(self, grid):

## Limits
- Time limit (s): 840.000
- Memory limit (MB): 64

## Constraints
- grid will contain between 1 and 50 elements, inclusive.
- Each element of grid will contain between 1 and 50 characters, inclusive.
- Each element of grid will contain the same number of characters.
- Each element of grid will contain only the characters '.' and '#'.

## Examples
0)
{ "####", "#..#", "#..#", "####" }
Returns: 1
Only one circle fits in this grid -- a circle of radius 1, in the center of the grid.

1)
{ "############", "###......###", "##.######.##", "#.########.#", "#.##..####.#", "#.##..####.#", "#.########.#", "#.########.#", "#.########.#", "##.######.##", "###......###", "############" }
Returns: 5
This is the example from the problem statement.

2)
{ ".........." }
Returns: 0
The grid must be at least two squares wide and tall in order for any circles to fit.

3)
{ "#######", "#######", "#######", "#######", "#######" }
Returns: 0

4)
{ "#####.......", "#####.......", "#####.......", "............", "............", "............", "............", "............", "............", "............" }
Returns: 4
A circle of radius 4 fits in this grid, as shown here:

5)
{ "#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.", "...#...#...#...#...#...#...#...#...#...#...#...#..", "#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.", ".#...#...#...#...#...#...#...#...#...#...#...#...#", "#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.", "...#...#...#...#...#...#...#...#...#...#...#...#..", "#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.", ".#...#...#...#...#...#...#...#...#...#...#...#...#", "#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.", "...#...#...#...#...#...#...#...#...#...#...#...#.#", "#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#." }
Returns: 0

6)
{ ".........................#........................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", "..................................................", ".................................................." }
Returns: 24
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.