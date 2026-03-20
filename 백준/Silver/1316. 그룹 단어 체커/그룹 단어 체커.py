n = int(input())
count = n  
for i in range(n):
    last = [-1] * 26
    word = input()
    for i in range(len(word)):
        idx = ord(word[i]) - ord('a') 
        if last[idx] == -1 :  #첫 등장! 
            last[idx] = i
        elif i - last[idx] > 1 : 
            count -= 1 
            break 

        last[idx] = i 

print(count)