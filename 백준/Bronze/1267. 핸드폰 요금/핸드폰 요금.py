n = int(input())
t = list(map(int, input().split()))

y_cost = 0
m_cost = 0

for i in t:
    y_cost += ((i // 30)+1) * 10
    m_cost += ((i // 60)+1) * 15

if y_cost < m_cost:
    print("Y", y_cost)
elif m_cost < y_cost:
    print("M", m_cost)
else:
    print("Y M",y_cost)