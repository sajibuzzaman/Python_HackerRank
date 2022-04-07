# Sample Input
#
# 1222311
# Sample Output
#
# (1, 1) (3, 2) (1, 3) (2, 1)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

if __name__ == '__main__':
    S = input()

    for k, g in groupby(S):
        print("(%d, %d)" % (len(list(g)), int(k)), end=" ")