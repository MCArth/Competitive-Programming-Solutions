Solution to https://open.kattis.com/problems/outing

Implemented using a variation of the 0-1 knapsack problem,
as every item can take any weight between a minimum and maximum.

Algorithm:

Every individual has someone they depend on. Individuals form chains or 'items'.
Part of these dependencies can form a loop, in which case every individual in the loop will be required to go
Example input 1: 2 3 1
This input forms a loop as you cannot send any of the individuals on the outing without the other members of the loop.
Hence minimum weight 3, maximum weight 4.

You can also have people who are not part of a loop, but either simply are offshoots of a loop that lead into a loop but
aren't depended on or are simply part of a chain of dependencies that end on someone who only wants to go with
themselves.

Example input 2:
2 3 1 2
The fourth individual here is not required to on the outing for the first three to go. Hence minimum weight 3, max
weight 4.

You can then split up all individuals into different items which are formed from individuals who have dependencies on
each other.

You can then implement a variation of the solution 0-1 knapsack problem where each item can take a weight between its
min weight and max weight.



Dynamic Programming portion of algorithm.

Stores previous results in 2-d array. Breaks problem size up into including the first i 'items' and the maximum amount 
of people who can go or weight, j.

Three cases to find the maximum weight for a given case.
Case 1: Including the item. New weight is max[i-1][j-weightCurrItem] + weightCurr Item.
This is because you look at the maximum only including previous items, and for the maximum weight where there will be 
space to include current item.
This is slightly modified however as the weightCurrItem can vary between the min and max value. This is dealt with using
 a for loop.

Case 2:

Not including the item, max[i-1][j]. Looks at max weight using previous items with the max for the current weight.

Case 3:

Current item is the first item included in the maximum. Can vary however, including the most that is possible between 
min and max.