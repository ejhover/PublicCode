# Warm-up: 5 min
# Stretch: 13 min
# Workout: 5 min
# Challenge: 25 min
def is_palindrome(stri):  
    return(("".join(i.lower() for i in stri if i.isalnum()))==("".join(i.lower() for i in stri if i.isalnum()))[::-1])
def foo(istring):
    p = '0123456789'
    os = ''
    for i in range(len(istring)):
        if istring[i] not in p:
            os += istring[i]
    return os
def first_letter():
    w,ans=" ",[]
    while w!="":
        if w.count(w[0])>1:
            ans.append(w)
        w=input("Enter word(Enter empty string to stop): ").lower()
    return ans
def igpay(words):
    vowel,ans="aeiou",[]
    for word in words.split():
        if word[0] in vowel:
            if word[-1].isalnum():
                ans.append(word+"way")
            else:
                ans.append(word[:-1]+"way"+word[-1])
        else:
            end=""
            for pos, i in enumerate(word):
                if i not in vowel:
                    end+=i
                else:
                    end=end.lower()
                    if not word[0].isupper():
                        if word[-1].isalnum():
                            ans.append(word[pos:]+end+"ay")
                            break
                        else:
                            ans.append(word[pos:-1]+end+"ay"+word[-1])
                            break
                    else:
                        if word[-1].isalnum():
                            ans.append((word[pos:]+end+"ay").capitalize())
                            break
                        else:
                            ans.append((word[pos:-1]+end+"ay"+word[-1]).capitalize())
                            break
                    
    return " ".join(ans)


if __name__ == "__main__":
    # m="mississippi"
    # print(m.count("s"))
    # print(m.replace("iss", "ox"))
    # print(m.index("p"))
    # print(foo("lkj12340hello"))
    # The function returns everthing in the given string that is not a integer
    # print(first_letter())
    # print(is_palindrome('Abba'), is_palindrome('Telat'), is_palindrome("MadaM I'm Adam"))
    # print(igpay("prepare"))
    print(igpay('Let the storm rage on, the cold never bothered me anyway!'))
