def two_es(lines):
    if len(lines) == 0:
        return False

    current_line = lines[0]
    count_of_e = 0
    for letter in current_line:
        if letter == 'e':
            count_of_e += 1

    if count_of_e == 2:
        return True
    else:
        remaining_lines = lines[1:]
        return two_es(remaining_lines)



if [two_es(['One line\n', 'Two lines\n', 'Three lines\n']),two_es(['here is a line\n', 'Another linE, starting with A\n', 'One MorE linE']),two_es([]),two_es(['More examples\n', 'Here there are two lines that work\n', 'This is one of them\n', 'This is not\n', 'Excellent'])] == [True,False,False,True]:
    print(True)
else:
    for i in range(100):
        print("THIS IS SO FALSE STOP THEM NOW THIS IS SO FALSE STOP THEM NOW THIS IS SO FALSE STOP THEM NOW THIS IS SO FALSE STOP THEM NOW THIS IS SO FALSE STOP THEM NOW")