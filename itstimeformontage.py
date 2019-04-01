uselessfuckingshit = input()
heroes = [int(a) for a in input().rstrip().split()]
villains = [int(a) for a in input().rstrip().split()]

if len(heroes) == 1:
    if heroes[0] >= villains[0]:
        print(0)
        quit()
    else:
        print(villains[0]-heroes[0])
        quit()

else:

    if heroes[0] > villains[0]:
        print(0)
        quit()
    else:
        days = villains[0]-heroes[0]

        
        for i in range(1, len(heroes)):
            if heroes[i] + days > villains[i]:
                print(days)
                quit()
            
            elif heroes[i] + days == villains[i]:
                continue
            
            else:
                print(days+1)
                quit()

print(days)

