# N 입력 받기 
n = int(input()) 

# N개의 숫자를 리스트에 저장하기 
nums = list(map(int,input().split()))

#최댓값을 저장할 변수 초기화 
max_ =  -1000000
#최솟값을 저장할 변수 초기화 
min_ = 1000000

#숫자를 하나씩 가져오면서, 
for i in nums:
    #내가 가지고 있는 최댓값보다 큰 값이 들어오면 바꾸기! 
    if max_  < i : 
        max_ = i

    #내가 가지고 있는 최소값보다 작은 값이 들어오면 바꾸기!  
    if min_ > i:
        min_ = i


print(min_,max_) 