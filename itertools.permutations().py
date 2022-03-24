# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()

output = ["".join(i) for i in permutations(S,int(k))]
# output.sort()
print("\n".join(sorted(output)))