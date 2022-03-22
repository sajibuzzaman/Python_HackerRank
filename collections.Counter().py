# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
if __name__ == '__main__':
    number_shoes = int(input())
    shoe_sizes = Counter(map(int, input().split()))
    if number_shoes >= len(shoe_sizes):
        customers = int(input())
        income = 0

        for _ in range(customers):
            size, price = map(int, input().split())
            if shoe_sizes[size]:
                income += price
                shoe_sizes[size] -= 1
        print(income)
    else:
        print('You input shoe size more than Number of shoes')