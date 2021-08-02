# 1085
x, y, w, h = map(int,input().split())
print(min(h-y,y,x,w-x))

# 3009
from collections import Counter
a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())
w_list = Counter([a,c,e])
h_list = Counter([b,d,f])
answer = []
for k, v in w_list.items():
    if v == 1:
        answer.append(k)
for k, v in h_list.items():
    if v == 1:
        answer.append(k)
for i in answer:
    print(i, end=" ")

# 4153
while True:
    a,b,c = map(int,input().split())
    if a ==0 and b == 0 and c ==0:
        break
    total_value = [a,b,c]
    max_value = max(total_value)
    total_value.remove(max_value)
    if max_value**2 == sum( [i**2 for i in total_value]):
        print("right")
    else:
        print("wrong")

# 1002
T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance = ((x2-x1)**2 + (y2-y1)**2) **0.5
    if distance == 0 and r1 == r2 : # 완전 접할때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance :  # 내접 or 외접
        print(1)
    elif abs(r1-r2) < distance < r1 +r2 :  # 두 점에서 만날 때
        print(2)
    else:
        print(0)
