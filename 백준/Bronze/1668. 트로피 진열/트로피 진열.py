n = int(input())
trophy = [] 

for i in range(n) : 
    trophy.append(int(input())) 
    
left = 0
left_max = 0
right = 0
right_max = 0 

for i in range(n) : 
    if trophy[i] > left_max : 
        left_max = trophy[i]
        left += 1 
 
    if trophy[n-i-1] > right_max :
        right_max = trophy[n-i-1]
        right += 1
        

print(left) 
print(right)
