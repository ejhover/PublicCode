# Emmet Hoversten
# hover114
# CSCI 1133 Section 050
# Assignment 4

# initialize pun_chars with all characters needing to be removed and filename for ignored words
PUN_CHARS = '[(.,;:\")]/]!?\n'
IGNORE_FILE = 'data/ignore_words.txt'

# loop through word list, lowercase every word and removes all of the pun_chars
def remove_punctuation_and_lower(word: str):
    wordlist = list(word)
    for pos, i in enumerate(wordlist):
        wordlist[pos] = i.lower()
        if i in PUN_CHARS:
            del wordlist[pos]
    return "".join(wordlist)

# loop through a list, remove all of the ignored words, and return the list
def get_words_from_file(words_filename, ignored_words_list=[]):
    file = open("repo-hover114/homeworks/hw04/" + words_filename, "r", encoding="utf8")
    words = file.read().split()
    for pos, i in enumerate(words):
        if i in ignored_words_list:
            del words[pos]
        else:
            continue
    file.close()
    return words

# loop through word list and add every word to a dictionary along with its count in the list
def get_word_frequency(word_list):
    """ return a dictionary with word/frequency """
    ans = {}
    for i in word_list:
        if i in ans.keys():
            ans[i]+=1
        else:
            ans[i]=1
    return ans

# create file and list 10 most popular words in a given file with the words given frequency
def save_popular_words(word_frequency, destination_file, k=10):
    popular_words = []
    for i in range(k):
        popular_word_key = [k for k, v in word_frequency.items() if v == max(word_frequency.values())]
        del word_frequency[popular_word_key[0]]
        popular_words.append(popular_word_key.pop(0))
        popular_word_key = []
    file = open("repo-hover114/homeworks/hw04/" + destination_file, "w")
    for pos, i in enumerate(popular_words):
        popular_words[pos] = i + "\n"
        file.write(popular_words[pos])
    file.close()

    


def main():
    """ Do not change this part. Only modify the functions above. """
    type_arr = ['Fake', 'True']
    for news_type in type_arr:
        source_file = f'data/{news_type}.csv'
        popular_words_file = f'data/{news_type}_popular_words.txt'

        # Process the file source_file and store every word on a single line dest_file
        # excluding the words in ignore_file
        ignored_words_list = get_words_from_file(IGNORE_FILE)
        word_list = get_words_from_file(source_file, ignored_words_list=ignored_words_list)
        word_frequency = get_word_frequency(word_list)

        # Save the top k most popular words
        save_popular_words(word_frequency, popular_words_file)
    """ Do not change this part """

if __name__ == "__main__":
    main()



