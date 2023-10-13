# Google Kickstart Round 2 Prob 1
import math

def solve():
    R, A, B = map(int, input().split())
    total_radius = R*R
    i = 1
    next_radius = R
    while next_radius >= 1:
        if (i%2) != 0:
            R *= A
            total_radius += (R*R)
            next_radius = (R / B)
        else:
            R //= B
            total_radius += (R*R)
            next_radius = (R * A)
        i+=1
    return total_radius * math.pi
        
for case in range(int(input())):
    print(f'Case #{case+1}: {solve()}')