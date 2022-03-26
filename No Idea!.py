# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
elements = input().split()
A = set(input().split())
B = set(input().split())

happiness = 0

for i in elements:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)