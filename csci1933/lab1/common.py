def common_letter(word):
    ans = (None, 0)
    for i in word:
        if word.count(i) > ans[1]:
            ans= (i, word.count(i))
    return ans
