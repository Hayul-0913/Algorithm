t = int(input())
for i in range (t):
    a,b = input().split()
    dist = []
    for j in range(len(a)) : 
        if a[j] <= b[j] : d = ord(b[j]) - ord(a[j])
        else : d = (ord(b[j])+26) - ord(a[j]) 
        dist.append(d) 
    print("Distances: ", end = "" )
    print(*dist)