'''
Input Format
A single line containing integer, N.

Constraints

Output Format
Print N-1 lines as explained above.

Sample Input

5
Sample Output

1
22
333
4444
'''

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i)//9)*i)