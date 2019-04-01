from sys import stdin

first = True
for x in stdin:
    if first:
        first = False
    else:
        x = [int(a) for a in x.rstrip().split()]
        count = x[1]+1
        for i in range(2, len(x)):
            if x[i] != count:
                print(i)
                break
            else:
                count += 1
                
