import os
# 4 min
def collatz(n):
    if n==1:
        return 1
    elif (n%2==0):
        return n+collatz(n//2)
    else:
        return n+collatz((n*3)+1)
# 8 min 
def two_es(lines):
    if not lines:
        return False
    if lines[0].count('e')==2:
            return True
    if len(lines)==1:
        if lines[0].count('e')==2:
            return True
        else:
            return False
    else:
        return two_es(lines[1:])
# 20 min so far
def get_targets(path, ans=[]):
    for file in os.listdir(path): 
        if os.path.isfile(path+'/'+file):
            if file.endswith('.txt'):
                with open(path+'/'+file, 'r') as f:
                    if two_es(f.readlines()):
                        ans.append(path+'/'+file)
        else:
            get_targets(path+'/'+file, ans)  #Go into a subdirectory   
    return ans