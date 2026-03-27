word = input().upper() #Apple -> APPLE

count = [0] * 26

for c in word:
    count[ord(c) - ord("A")] += 1 #ord --> 알파벳을 숫자로 변환 

idx = 0 
ans = "A"

for i in range(1,26) : 
    #max 값 찾기 
    if count[i] > count[idx]: 
        idx = i 
        ans = chr(i+ ord("A")) #chr --> 숫자를 알파벳으로 변환 
    elif count[i] == count[idx]: 
        ans = "?"

print(ans) 
