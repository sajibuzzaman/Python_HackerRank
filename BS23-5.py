# String stings
'''
Brain Station-23 will give you a string x and there will be z queries. Queries can be two types:
Type 1: 1 a p
Type 2: 2 m n k
In Type 1: a-th character will be turned into p.
In Type 2: Output the number of times k happens in x as a substring of x starting from m to n inclusive.

Input
First line will contain x(1 ≤ |x| ≤ 10^5).
Second line will contain z(1 ≤ z ≤ 10^5).
Next z lines will contain any of two types queries.

1 ≤ a ≤ |x|
1 ≤ m ≤ n ≤ |x|

The sum of all |k| is at most 10^5
Every string is 1-indexed

Output
For each type 2, show the output in separate lines.

Sample 1
abcdcbc
5
2 1 7 bc
1 4 b
2 4 7 bc
1 2 a
2 1 4 aa

Sample 2
2
2
1
'''