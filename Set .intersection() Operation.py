# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    n_roll = set(map(int, input().split()))
    b = int(input())
    b_roll = set(map(int, input().split()))

    result = n_roll.intersection(b_roll)

    print(len(result))