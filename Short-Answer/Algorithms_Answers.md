#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)O(n^3).
The number of loops will depend on n* n *n.
This is common with algorithms that involve nested iterations over the data set.

b)O(n^2).
Nested "for loops" based on "n" in both loops(nested).

c)O(N).
Called recusively based on bunnies - 1, base case bunnies == 0
Describes an algorithm whose performance will grow linearly and in direct proportion to the size of the input data set.

## Exercise II

Step 1: Got to the middle floor.

Step 2 - MAIN: Drop an egg:

    Step 2 - A:
    If it breaks, go half way up the top remaining floors.

    Step 2 - B:
    If it does not break, go half way down the bottom remaining floors.

    Step 2 - C:
    Repeat Step 2 - MAIN.

#---// Runtime complexity of your solution.//-----#

Time Complexity:

O(log n), the number of possible floors is cut in half on each call of the recusive function

#-----------// code solution // ------------#

<!-- f = floors

def drop_at_midpoint(f):

    mid = current_floor = midpoint_of_floors
    t = top_half_of_current_floors
    b = bottom_half_of_current_floors

    if no_of_floors = 1:
        return current_floor

    if egg_breaks:
        drop_at_midpoint(b)
    else:
        drop_at_midpoint(t) -->
<!--
def drop_at_midpoint(floor, egg, down_floor, up_floor):
    mid = (down_floor + up_floor) // 2
    curr = current_floor


    if floor[curr] == mid:
        return mid -->
