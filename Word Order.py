# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

order = OrderedDict()

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        word = input()
        if word in order:
            order[word] += 1
        else:
            order[word] = 1

    print(len(order))

    L = []
    for word, frequency in order.items():
        L.append(str(frequency))

    print(' '.join(L))