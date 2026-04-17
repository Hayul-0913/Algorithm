heights = [] 
for i in range(9):
    h = int(input())
    heights.append(h)
total = sum(heights)

for i in range(9): 
    for j in range(9):  
        if i == j : continue
        if total - heights[i]-heights[j] == 100:
            ans = [] 
            for k in range(9) : 
                if k == i or k == j : continue
                ans.append(heights[k])
            ans.sort() 
            for a in ans : 
                print(a) 
            exit() 