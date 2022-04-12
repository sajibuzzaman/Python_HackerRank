'''
Welcome To the Coding Challange Of Brain Station-23. Marajul Is a newbie programmer of brain station-23. Dhurba is a very tallented progeammer who is also the mentor of Marajul. Dhurba Gave him a problem regarding array, Especially about Friend array. But As He is Newbie He failed multiple time Calculate the friend array.

F=[f_1, f_2, f_3, ...... f_N]F=[f
1
​
 ,f
2
​
 ,f
3
​
 ,......f
N
​
 ] is called Friend array of A = [a_1, a_2, a_3, ...... a_N]A=[a
1
​
 ,a
2
​
 ,a
3
​
 ,......a
N
​
 ] if

For all i (1 \le i \le N)i(1≤i≤N), F_i = A_N - A_iF
i
​
 =A
N
​
 −A
i
​

|F| = |A|∣F∣=∣A∣, Here |F|∣F∣ means Size of Array FF.
To help marajul You are Given An Array AA of size N. You have to Check the Friend Array of AA is Sorted in descending order or not. [An array Has only one Friend array]

An Array A[a_1, a_2, a_3, ..... a_n]A[a
1
​
 ,a
2
​
 ,a
3
​
 ,.....a
n
​
 ] is descending if for all i(1 \le i < N),i(1≤i<N), A_i \ge AA
i
​
 ≥Ai + 1
 
Input
The first line of the input will contain N (0 < N < 100) size of the array

The following line will contain NN integers denoting the array AA (1\le A_i \le 10001≤A
i
​
 ≤1000)

Output
Print “Yes” if the Friend Array is sorted in descending order otherwise “No”.

sample
Input
3
1 2 3

Output
Yes
'''

# Driver Code
if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    # Array is sorted in descending order
    arr1 = sorted(arr)[::-1]
    print(arr1)
    # Check is it equal to sorted order then print Yes otherwise print No
    if arr == arr1:
        print('Yes')
    else:
        print('No')