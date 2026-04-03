n = int(input())
for i in range(n):
    s = input()
    score = 0
    c = 0 
    for con in s:
        if con == "O": #"O" 
            c += 1  #2
            score += c 
        else : #"X"
            c = 0 
    print(score) 