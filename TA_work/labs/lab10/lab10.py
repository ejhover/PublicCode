# 6 min
def word_freq(fname):
    fp, counts = open(fname, 'r'), {}
    for line in fp.readlines():
        words = line.split()
        for word in words:
            if word in counts.keys():
                counts[word]+=1
            else:
                counts[word] = 1
    fp.close()
    return counts
# 6 min
def morse(text):
    ans=""
    morse_dictionary={'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}
    morse_dictionary = dict([(value, key) for key, value in morse_dictionary.items()])
    
    for i in text.split("/"):
        letters = i.split()
        for j in letters:
            ans+=morse_dictionary[j]
        ans+=" "
    return ans
#15 min

# total = costs['Chicago']['Las Vegas'] + costs['Las Vegas']['Dallas']
def cheapest(costs, origin, destination):
    ans=float('inf')
    for i in costs[origin].keys():
        if destination in costs[i].keys():
            if costs[origin][i]+costs[i][destination]<ans:
                ans=costs[origin][i]+costs[i][destination]
    if destination in costs[origin]:
        if costs[origin][destination]<ans:
            ans=costs[origin][destination]
    return ans
# 4 min
def rank_suit_count(cards):
    rank={}
    suit={}
    for i in cards:
        if i[0] in rank:
            rank[i[0]]+=1
        else:
            rank[i[0]]=1
        if i[1] in suit:
            suit[i[1]]+=1
        else:
            suit[i[1]]=1
    return [rank, suit]




