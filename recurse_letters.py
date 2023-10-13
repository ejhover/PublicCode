global COMBINATIONS
COMBINATIONS = []
def word_possibilities(remaining, chosen):
    if len(remaining) == 0:
        COMBINATIONS.append(chosen + remaining)
    else:
        for pos, i in enumerate(remaining):
            new_chosen = chosen
            new_chosen += i
            new_remaining = remaining[0:pos]+remaining[pos+1:]
            word_possibilities(new_remaining, new_chosen)

def main():
    word_possibilities('emmet', "")
    print(COMBINATIONS)
if __name__ == "__main__":
    main()