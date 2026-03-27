
T = int(input())
for i in range(T):
    input()
    n = int(input())
    total = 0
    for j in range(n):
        candy = int(input())
        total += candy 
    if total % n  == 0:
        print("YES")
    else:
        print("NO")
