# 5 min
def cross(u, v):
    return [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]

# 10 min
def all_names(first_names, last_names, length):
    ans = []
    for i in first_names:
        for j in last_names:
            ans.append(f'{i} {j}')
    return [i for i in ans if len(i)==length]

#20 min
def change_key(notes, up):
    ans = []
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    for i in notes:
        if (scale.index(i)+(up%12))>11:
            ans.append(scale[scale.index(i)+(up%12)-12])
        else:
            ans.append(scale[scale.index(i)+(up%12)])
    return ans
