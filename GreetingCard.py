# solution to: https://open.kattis.com/problems/greetingcard

waste = input()
from sys import stdin
points = {}
chg = [[1118, 1680], [1680, 1118]]
count = 0
for x in stdin:
    x = tuple(int(a) for a in x.rstrip().split())

    points[x] = 1

    if points.get((x[0]+2018, x[1])) == 1:
        count += 1
    if points.get((x[0]-2018, x[1])) == 1:
        count += 1
    if points.get((x[0], x[1]+2018)) == 1:
        count += 1
    if points.get((x[0], x[1]-2018)) == 1:
        count += 1

    for a in chg:
        for b in [(1,1), (-1,-1),(-1,1),(1,-1)]:
            if points.get((x[0]+a[0]*b[0], x[1]+a[1]*b[1])) == 1:
                count += 1

print(count)
