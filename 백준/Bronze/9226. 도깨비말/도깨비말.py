v = "aeiou"
while True:
    w = input()
    if w == "#":
        break
    # for문을 이용해서 모음이 등장하는 위치를 i에 저장하기 
    check = -1 
    for i in range(len(w)) : 
        if w[i] in "aeiou" :  # w[i] == "a" or w[i] == "e" .. 
            check = 1 
            break 
    if check == -1:
        print(w+"ay")
    else : 
        print(w[i:] +w[:i] + "ay")