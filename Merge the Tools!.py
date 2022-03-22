def merge_the_tools(string, k):
    # your code goes here
    L = []
    flag = 0
    for i in string:
        flag += 1
        if i not in L:
            L.append(i)
        if flag == k:
            print(''.join(L))
            L = []
            flag = 0


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)