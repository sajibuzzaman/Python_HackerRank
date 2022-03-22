# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
columns_name = input().split()
std_details = namedtuple('std_details', columns_name)

result = 0
for i in range(n):
    ID, MARKS, CLASS, NAME = input().split()
    std = std_details(ID, MARKS, CLASS, NAME)
    result += int(std.MARKS)

print("%.2f" % (result/n))