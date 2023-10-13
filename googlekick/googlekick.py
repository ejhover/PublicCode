
'''def solve():
    num_bags, num_kids = map(int, input().split())
    candy_in_bags = [int(i) for i in input().split()]
    return (sum(candy_in_bags)%num_kids)


for i in range(int(input())):
    print(f'Case #{i+1}: {solve()}')'''
'''
2
7 3
1 2 3 4 5 6 7
5 10
7 7 7 7 7
'''
'''
def solve():
    ans = 0
    d = int(input())
    v = [int(i) for i in input().split()]
    for pos in range(len(v)):
        if ((pos == 0) or (v[pos]>max(v[:pos]))) and ((pos == (len(v)-1)) or (v[pos]>v[pos+1])):
            ans += 1

    return ans



for i in range(int(input())):
    print(f'Case #{i+1}: {solve()}')'''

'''def number_of_record_breaking_days(number_of_days, visitors):
    ans = 0
    v = visitors
    for pos in range(len(v)):
        if ((pos == 0) or (v[pos]>max(v[:pos]))) and ((pos == (len(v)-1)) or (v[pos]>v[pos+1])):
            ans += 1

    return ans

def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    number_of_days = int(input())
    vistors = list(map(int, input().split()))

    ans = number_of_record_breaking_days(number_of_days, vistors)

    print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()'''

def record_breaker():
    N = input()
    V = map(int, raw_input().strip().split())

    result = max_v = 0
    for i, v in enumerate(V):
        if (i == 0 or v > max_v) and (i+1 == len(V) or v > V[i+1]):
            result += 1
        max_v = max(max_v, v)
    return result

for case in range(input()):
    print(f'Case #{case+1}: {record_breaker()}')

'''
4
8
1 2 0 7 2 0 2 0
6
4 8 15 16 23 42
9
3 1 4 1 5 9 2 6 5
6
9 9 9 9 9 9
'''