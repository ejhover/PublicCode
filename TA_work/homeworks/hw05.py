def character_search(string_a, string_b, string_c):
    new_string = ''
    i = 0
    j =0 
    #y=0
    while i < len(string_a):
        #j = 0
        while j < len(string_b):
            if string_a[i]== string_b[j]:
                y = 0
                while y < len(string_c):
                    if string_a[i] == string_b[j] and string_a[i] !=string_c[y]:
                        new_string += string_a[i]
                        i += 1
                        y+= 1
                        j += 1
                        #new_string += string_a[i]
                       # print(i, j, y, new_string)
                    else:
                        i += 1
                        j += 1
                        y += 1
                       # print(i, j, y, new_string)
            else:
                 j += 1
                 i += 1            
           # j += 1
        #    j += 1
        i += 1
    return new_string