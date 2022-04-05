# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    M = int(input())
    a = set(list(map(int, input().split())))
    N = int(input())
    b = set(list(map(int, input().split())))
    result = a.difference(b)
    result2 = b.difference(a)
    result.update(result2)
    # f_result = a ^ b
    # print(f_result)
    for i in sorted(result):
        print(i)