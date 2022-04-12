'''
You will get an array of n numbers. Find out the k-th maximum number of the array.

Suppose you have 9 2 5 1 10. Here 1st maximum number is 10, second is 9, third is 5 and so on.

Input
First line contain n and k (1 ≤ n ≤ 1000, 1 ≤ k ≤ n) The second line contains n space-separated integers ai (0 ≤ ai ≤ 100), ai is the i-th number of the array.

Output
Print the k-th maximum number of the array.

Sample
Inpu
15 1
0 78 24 24 61 60 0 65 52 57 97 51 56 13 10

Output
97
'''

# Function to print Kth Maximum Number
def kMax(ai, k):
    # sort the given list and reverse=True
    ai = sorted(ai, reverse=True)

    # Print the first kth largest elements
    for i in range(k):
        print(ai[i], end=" ")

# Driver Code
if __name__ == '__main__':
    n, k = map(int, input().split())
    ai = map(int, input().split())
    kMax(ai, k)

