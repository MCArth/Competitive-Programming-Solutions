from sys import stdin

hehexd = True
for inp in stdin:
    if hehexd:
        first = inp.rstrip().split()[1]
        hehexd = False

    else:
        select = inp.rstrip().split()

        nums = {'Q': 10, 'J': 10, 'K': 10, 'A': 11}

        iOfSel = []
        i = int(first)
        for x in range(len(select)):
            if select[x].isdigit():
                iOfSel.append(i)
                i += int(select[x])
            else:
                iOfSel.append(i)
                i += nums[select[x]]

        if iOfSel[-1] < 10:
            probs = [0] * 10
        else:
            probs = [0] * iOfSel[-1]
    
        for x in iOfSel:
            probs[x-1] = 1

        for i in range(len(probs) - 1, -1, -1):
            if probs[i] == 0:
                for x in range(2, 12):
                    if i + x <= iOfSel[-1] - 1:
                        if x != 10:
                            probs[i] += (1/13) * probs[i+x]
                        else:
                            probs[i] += (4/13) * probs[i+x]
        
        
        total = 0
        for i in range(10):
            total += probs[i]
        print(total/10)

        hehexd = True

