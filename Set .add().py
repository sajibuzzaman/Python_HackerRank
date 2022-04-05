# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N = int(input())
    S = set()
    for _ in range(N):
        country = input()
        S.add(country)

    print(len(S))