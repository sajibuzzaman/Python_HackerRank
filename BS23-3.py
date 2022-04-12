'''
Brain Station-23 is going to Open A new Branch Office at Banasree. For New Branch Office NN new software engineers have been Appointed. Each Employee Has a unique employee Id at the brain Station. To Operate the Office Properly the Abdul Motaleb Sohel, Manager of HR Wants to form some teams from newly appointed people. But there are some conditions to forming a team.

The size of any team |T|∣T∣ can be from 11 to NN which means 1 \le |T| \le N1≤∣T∣≤N, Here |T|∣T∣ mean size of Team TT
A team Can be only formed with consecutive id members. Suppose TT is a team and the smallest id member is SmSm and The Largest id member of any team is LgLg, Now The team Must Contain All members having ID SmSm to LgLg And the Size of the team must be (Lg - Sm +1)(Lg−Sm+1)
The Summation of the weight of All members of any team should be less than XX ( will be given at input).
Now You have Appointed to Count How many ways you can form a team under this condition.

Input
in the first line TT, number of test cases.

For each test case, the first line contains NN, XX (1 \le N \le 10^51≤N≤10
5
 ,1 \le X \le 10^91≤X≤10
9
 ) the number of Employees and the number given in the problem statement.

the second line contains NN separated integers Weight (W_iW
i
​
  ) of employee having ID - i (1 \le W_i \le 10^91≤W
i
​
 ≤10
9
 ).

Output
For each test case output the number of ways a team can be formed under this condition.

Sample 1
Input
2
1 4
3
2 4
1 5

Output
1
1
'''