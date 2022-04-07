'''
Sample Input
4
a a c d
2

Sample Output
0.8333
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    latters = input().split()
    K = int(input())

    combination = list(combinations(latters, K))
    a = [word for word in combination if 'a' in word]

    # print(a)
    # print(combination)
    print('%.3f' % (len(a) / len(combination)))
