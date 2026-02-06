num = [0] * 31
for i in range(28):
    num[int(input())] = 1

for i in range(1,31):
    if num[i] == 0 :
        print(i)