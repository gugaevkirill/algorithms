# Backpack

### Definition
Given a set of different items, each one with an associated value and weight, determine which items you should pick in order to maximize the value of the items without surpassing the capacity of your backpack.

### Input
Backpack weight, tuple of weights & tuple of values of possible items.

### Output
Maximum value of items in backpack

### Examples:
#### All items:
10
(1, 2, 3)
(2, 2, 2)
answer: 6

#### Max valuable item
8
(2, 2, 2, 2, 7)
(1, 1, 2, 1, 25)
answer: 25

#### Not so obvious set
6
(4, 3, 3)
(8, 5, 5)
answer: 10

#### Full backpack
8
(1, 1, 2, 2, 3)
(1, 1, 2, 2, 3)
answer: 8
