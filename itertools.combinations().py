# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, k = input().split()

for i in range(1,int(k)+1):
    output = ["".join(i) for i in combinations(sorted(S),i)]
    print("\n".join(output))