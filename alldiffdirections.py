from math import sin, cos, pi

while True:
    try:
        n, ang, ansx, ansy = int(input()), 0, 0, 0
    except:
        break
    for _ in range(n):
        try:
            lis = [float(i) for i in input().split() if not i.isalpha()]
            x, y = lis.pop(0), lis.pop(0)
        except:
            break
        for pos, i in enumerate(lis):
            if (pos%2)==0:
                x+=lis[pos+1]*cos(i*(180/pi))
                y+=lis[pos+1]*sin(i*(180/pi))
        ansx+=x
        ansy+=y
    try:
        print("yoo", ansx/n, ansy/n)
    except:
        pass
    






'''
3
87.342 34.30 start 0 walk 10.0
2.6762 75.2811 start -45.0 walk 40 turn 40.0 walk 60
58.518 93.508 start 270 walk 50 turn 90 walk 40 turn 13 walk 5
2
30 40 start 90 walk 5
40 50 start 180 walk 10 turn 90 walk 5
0
'''