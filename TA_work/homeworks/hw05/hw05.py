# Emmet Hoversten

# 10 minutes
def greater_by_one_for(a_string):
    ans=""
    for i in a_string:
        ans+=str(((int(i)+1)%10))
    return ans
def greater_by_one_while(a_string):
    ans, n="", 0
    while n<len(a_string):
        ans+=str(((int(a_string[n])+1)%10))
        n+=1
    return ans
# 9 minutes
def count_of_sums(lower, upper, sum_val):
    a, ans = list(range(lower, upper+1)), 0
    for i in a:
        if sum_val-i in a:
            ans +=1
    return ans
# 8 minutes
def character_search(string_a, string_b, string_c):
    ans=""
    for i in string_a:
        if i in string_b and i not in string_c:
            ans+=i
    return ans
# 
