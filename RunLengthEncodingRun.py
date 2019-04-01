a = input().rstrip().split()
b = a[1]

if a[0] == 'E':
    p = 0
    out = ""
    count = 1
    prev = ''
    while p < len(b):
        if b[p] == prev:
            count += 1
        else:
            out += str(count) + b[p]
            count = 1
            prev = b[p]

        p += 1
        
    out += str(count)
    out = out[1:]

else:
    point = 0
    out = ""
    while point < len(b):
        out = "".join([out, "".join([b[point] for l in range(int(b[point+1]))])])
        point += 2

print(out)
