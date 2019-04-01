from sys import stdin

first = True
for x in stdin:
    if first:
        first = False
    else:
        dOrE = x[0]
        x = list(x[2:-1])
        
        if dOrE == 'e':
            
            for i in range(1, len(x)):
                if ord(x[i]) == 32:
                    chrval = 0
                else:
                    chrval = ord(x[i])-96
                    
                if ord(x[i-1]) == 32:
                    prev = 0
                else:
                    prev = ord(x[i-1])-96

                val = (chrval + prev)%27
                
                if val == 0:
                    x[i] = " "
                else:
                    x[i] = chr(val+96)
            print(*x, sep='')
                
        else:
            for i in range(len(x)):
                x[i] = ord(x[i])-96
                if x[i] == -64:
                    x[i] = 0

            oldx = x.copy()
            for i in range(1, len(x)):
                x[i] = (x[i]-oldx[i-1])%27

            
            for i in range(len(x)):
                if x[i] == 0:
                    x[i] = ' '
                else:
                    x[i] = chr(x[i]+96)

            print(*x, sep = '')
            
