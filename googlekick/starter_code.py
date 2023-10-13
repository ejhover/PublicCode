# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4a94/0000000000b54d3b
def count_yes(N, Q, blocks, questions):
    # TODO: Complete this function and return the number of "yes" answers.
    yes_answers = 0
    for i in (questions):

    return yes_answers
def main():
    T = int(input())
    for T in range(1, T + 1):
        N, Q = map(int, input().split())
        blocks = input()
        questions = []
    for i in range(Q):
        L, R = map(int, input().split())
        questions.append((L, R))

        answer = count_yes(N, Q, blocks, questions)

        print(f'Case #{T}: {answer}')

if __name__ == '__main__':
  main()
