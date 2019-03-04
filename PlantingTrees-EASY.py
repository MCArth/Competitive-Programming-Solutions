import sys

# Solution to: https://open.kattis.com/problems/plantingtrees

p=0
for x in sys.stdin:
    if p == 1:
        trees = [int(a) for a in x.rstrip().split()]
    
    p+=1

trees.sort(reverse=True)
maxDay=0
for i in range(len(trees)):
    if trees[i]+i+1 > maxDay:
        maxDay = trees[i]+i+1

print(maxDay+1)
