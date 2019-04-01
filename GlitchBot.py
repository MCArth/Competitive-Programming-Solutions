targ = [int(a) for a in input().rstrip().split()]
waste = input()

from sys import stdin
inst = []
for x in stdin:
    inst.append(x.rstrip())


for i1 in range(len(inst)):
    newInst = inst.copy()
    if inst[i1] == "Forward":
        trying = ["Left", "Right"]
    elif inst[i1] == "Right":
        trying = ["Left", "Forward"]
    elif inst[i1] == "Left":
        trying = ["Forward", "Right"]

    for a in trying:
        newInst[i1] = a
        pos = [0, 0]
        dire = 0
        for i in newInst:
            if i == "Forward":
                if dire == 0:
                    pos[1] += 1  
                elif dire == 1:
                    pos[0] += 1
                elif dire == 2:
                    pos[1] -= 1
                elif dire == 3:
                    pos[0] -= 1
            elif i == "Left":
                dire = (dire-1)%4
            elif i == "Right":
                dire = (dire+1)%4

        if targ == pos:
            print(str(i1+1) + " " + a)
            quit()

