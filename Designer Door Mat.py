# # Enter your code here. Read input from STDIN. Print output to STDOUT
# I = input().split()
# N = int(I[0])
# M = int(I[1])
# X = ".|."
#
# for i in range(N//2):
#     print(((X*i) + X + (X*i)).center(M, '-'))
#
# print('WELCOME'.center(M, '-'))
#
# for i in range(N//2):
#     print(((X * ((N//2) - 1 - i)) + X + (X * ((N//2) - 1 - i))).center(M, '-'))

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
for i in range(1, N, 2):
    print((i * ".|.").center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, '-'))