max_score = 0
winner = 0

for i in range(1,6): 
    score = list(map(int,input().split()))
    total = 0 
    for j in range(4):
        total += score[j] 
    
    if max_score < total : 
        winner = i 
        max_score = total 
    

print(winner,max_score)