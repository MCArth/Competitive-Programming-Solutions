from sys import stdin
first = True
for x in stdin:
    if first:
        first = False
    else:
        n = int(x.rstrip())
        if n == 0:
            print("0")
            continue
        
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))

        thingy = ''.join(reversed(nums))
        leading0 = 0
        for i in range(len(thingy)):
            if thingy[i] != 0:
                break
            else:
                leading0 += 1
        print(thingy[leading0:])

