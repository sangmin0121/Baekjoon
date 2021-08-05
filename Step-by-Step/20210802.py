# 2231
N = int(input())
answer=[]
for i in range(1,N):
    if N == i + sum(map(int,str(i))):
        answer.append(i)
        print(i)
        break
if len(answer) == 0:
    print(0)


# 7568
N = int(input())
w_t_list = []
answer=[]
for i in range(N):
    w_t_list.append(input().split())

for i in range(N):
    cnt = 1    
    for k in range(N):
        if w_t_list[i][0] < w_t_list[k][0] and w_t_list[i][1] < w_t_list[k][1]:
            cnt+=1
    answer.append(cnt)
for i in answer:
    print(i, end=" ")


# 1436
N = int(input())
cnt=0
six_n = 666
while True:
    if '666' in str(six_n):
        cnt+=1
    if cnt == N:
        print(six_n)
        break
    six_n+=1