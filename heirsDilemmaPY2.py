inp = [int(a) for a in raw_input().rstrip().split()]

total = 0
for num in range(inp[0], inp[1]+1):
    cont = False
    digits = {}
    for x in str(num):
        if x not in digits:
            digits[x] = 0
        else:
            cont = True
            break
        
    if cont:
        continue

    div = True
    for dig in digits:
        dig = int(dig)
        if dig != 0 and num % dig != 0:
            div = False
        elif dig == 0:
            div = False

    if div:
        total += 1

print(total)
