import sys
from math import cos, radians

# Solution to: https://open.kattis.com/problems/mountainbiking

p = 0
segments = []
for x in sys.stdin:
    x = x.rstrip().split()
    if p == 0:
        g = float(x[1])
    else:
        segments.append(x)
    
    p += 1

speed = 0
speeds = []
for x in range(len(segments)-1, -1, -1):
    speed = pow((pow(speed,2))+(2*int(segments[x][0])*g*cos(radians(int(segments[x][1])))),(1/2))
    speeds.append(speed)
for x in range(len(speeds)-1, -1, -1):
    print(speeds[x])
