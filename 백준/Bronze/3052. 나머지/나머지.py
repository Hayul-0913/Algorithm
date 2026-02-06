

num = [0] * 42
for i in range(10):
    num[int(input())%42] = 1

count = 0 
for i in range(42):
    if num[i] > 0 :
        count += 1 

print(count)