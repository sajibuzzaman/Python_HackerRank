'''
Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
Sample Output

206
Explanation

Picking 5 from the 1st list,  from the 2nd list and 10 from the 3rd list gives the maximum S value equal to (5^2+9^2+10^2)%1000 = 206.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

# if __name__ == '__main__':
#     K, M = map(int, input().split())
#
#     L = []
#     for _ in range(K):
#         N = list(map(int, input().split()))
#         L.append(max(N))
#
#     S = 0
#     for i in L:
#         S += int(i) ** 2
#
#     print(S % M)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    K, M = map(int, input().split())

    L = []
    for _ in range(K):
        N = list(map(int, input().split()))
        del N[0]
        L.append(N)


    def sqr(n):
        return n ** 2


    P = list(product(*L))

    R = []
    for i in P:
        result1 = sum(map(sqr, [a for a in i]))
        result2 = result1 % M
        R.append(result2)

    print(max(R))
