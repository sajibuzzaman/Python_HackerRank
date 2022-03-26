# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N = int(input())
item = OrderedDict()

for _ in range(N):
    name, space, price = input().rpartition(" ")
    # if name in item:
    #     item[name] += int(price)
    # else:
    #     item[name] = int(price)
    item[name] = item.get(name, 0) + int(price)

for name, price in item.items():
    print(name, price)