max_ = -1 
idx = -1

for i in range(1,10) : # 0,1,2,3,4,5,6,7,8,9
    num = int(input())
    if num > max_ : 
        idx = i 
        max_ = num 


print(max_)
print(idx)
    