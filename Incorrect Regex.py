# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        try:
            print(bool(re.compile(input())))
        except:
            print('False')
