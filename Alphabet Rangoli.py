import string
alphabet_string = string.ascii_lowercase

def print_rangoli(size):
    # your code goes here
    L = []
    for i in range(size):
        result = '-'.join(alphabet_string[i:size])
        L.append((result[::-1]+result[1:]).center(4*n-3, '-'))
        # print(result)
    # print(L)
    print('\n'.join(L[::-1]+L[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)