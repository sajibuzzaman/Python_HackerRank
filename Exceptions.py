# Enter your code here. Read input from STDIN. Print output to STDOUT
T = input()

for _ in range(int(T)):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except Exception as e:
        print("Error Code:", e)