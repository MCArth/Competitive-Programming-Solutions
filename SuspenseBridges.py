from math import cosh, sinh

inp = [int(a) for a in input().rstrip().split()]

top = 1000000
bot = 0

curr = 0
s = inp[1]
while round(curr, 9) != s:
    a = ((top-bot)/2)+bot
    
    
    curr = a*cosh(inp[0]/(2*a))-a
    
    if curr > s:
        bot = a
    elif curr < s:
        top = a

print(2*a*sinh(inp[0]/(2*a)))
