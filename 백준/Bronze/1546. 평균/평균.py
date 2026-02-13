n = int(input())
scores = list(map(int, input().split()))

M = max(scores)
for i in range(n):
    scores[i] = scores[i]/M*100

total = 0

for i in range(n): 
    total = total + scores[i]
print(total/n)