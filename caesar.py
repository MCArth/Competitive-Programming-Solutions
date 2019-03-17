first = input().rstrip()
count = 0
for shift in range(26):
    noIs = True
    for char in first:
        newOrd = ord(char)+shift
        if newOrd > 122:
            newOrd -= 26
        
        if chr(newOrd) == 'i':
            noIs = False
            break

    if noIs:
        count += 1

if count > 0:
    print(count)

else:
    print("impossible")
