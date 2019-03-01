# Solution to: https://open.kattis.com/problems/compiler

num = int(input().rstrip())
temp = num

binary = [128, 64, 32, 16, 8, 4, 2, 1]
binNum = [0] * 8

for i in range(len(binary)):

    if temp >= binary[i]:
        temp -= binary[i]
        binNum[7-i] = 1

if num != 0:

    print('ST X')
    
    numCreated = 0
    i = 0
    stackSize = 0
    
    while numCreated < num:
        if binNum[i] == 1:
            numCreated += binary[7-i]
            binNum[i] = 0
            stackSize += 1
            
            print('PH X')

        else:
            print('PH X\nPH X\nAD\nPL X')
            i += 1


    for x in range(stackSize-1):
        print('AD')

    print('PL X')

else:
    print('ZE X')

print('DI X')
