# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab, bc = int(input()), int(input())

result = math.atan(ab/bc)
print(round(math.degrees(result)), chr(176), sep='')