import random
# 5 minutes
def div27(num):
    out = False
    for i in range(2,8):
        if num % i == 0:
            return True
    return out
def mul(a,b):
    ans=0
    for i in range(a):
        ans+=b
    return ans
def mul2(a,b):
    ans=i=0
    while i<a:
        ans+=b
        i+=1
    return ans
# 10 minutes
def expo(x,y):
    prod,i = 1,0
    while i<y:
        total = j = 0
        while j<x:
            total += prod
            j+=1
        prod = total
        i+=1
    return prod
# 12 min
def takeaway():
    objects=21
    while objects > 0:
        take=99
        while take>objects:
            take=random.randint(1,3)
            print(f'{objects} objects remain, Ill take {take}')
            objects-=take
            if objects <= 0:
                print("Computer Wins!")
                return
            player = int(input(f'{objects} objects remain, choose 1, 2, or 3: '))
            objects-=player
            if objects <= 0:
                print("You Win!")
                return
    






if __name__ == '__main__':
    # print(div27(15)) #Should return True
    # print(mul(5, 3)) #should output 15
    # print(mul2(5, 3)) #should output 15
    # print(mul(20, 3)) #should output 15
    # print(mul2(20, 3)) #should output 15
    # print(expo(3,3))
    takeaway()

