# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = map(int, input().split())
B = map(int, input().split())
A = sorted(list(set(A)))
B = sorted(list(set(B)))

print(*(product(A, B)))