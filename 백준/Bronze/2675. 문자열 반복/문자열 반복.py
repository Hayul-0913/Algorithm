
n = int(input())
for i in range(n):
    R, S = input().split() #"AAABBBCCC"
    R = int(R)
    ans = "" 
    for j in S : 
        ans += j * R 
    print(ans)