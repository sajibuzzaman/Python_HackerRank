# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == '__main__':
    N = int(input())
    d = deque()

    for _ in range(N):
        value = input().split()

        if value[0] == 'append':
            d.append(int(value[1]))
        elif value[0] == 'pop':
            d.pop()
        elif value[0] == 'popleft':
            d.popleft()
        elif value[0] == 'appendleft':
            d.appendleft(int(value[1]))

    print(*d)