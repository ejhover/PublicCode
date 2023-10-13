# https://edabit.com/challenge/RB6iWFrCd6rXWH3vi

def longest_substring(digits):
    alternations = []
    binary = [0 if (int(i)%2==0) else 1 for i in digits]
    substr = ""
    for pos, curr in enumerate(binary):		     
        nex = binary[pos+1]		
        if curr != nex:
            substr += digits[pos]
            substr += digits[pos+1]
        if curr == nex:
            if len(substr)>1:
                alternations.append(substr)
            substr = ""
        if (pos+1) == len(binary)-1:
            if len(substr)>1:
                alternations.append(substr)
            break

    lengths = [len(i) for i in alternations]
    return(alternations[lengths.index(max(lengths))][::2] + alternations[lengths.index(max(lengths))][-1])

print(longest_substring("721449827599186159274227324466")) # "272163254"