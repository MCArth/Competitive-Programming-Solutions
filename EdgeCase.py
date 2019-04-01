from sys import stdin
from math import factorial as fact

for x in stdin:
    x = int(x)

    total = 0
    use = True

    for i in range(int(x/2)):
        total += fact(x)/(fact(x-2*i)*fact(2*i))

    print(total)
