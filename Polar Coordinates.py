# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import polar, phase

Z = complex(input())

print(abs(Z)) #r = absulate value
print(phase(Z)) # = phase

# for i in polar(Z):
#     print(i)
