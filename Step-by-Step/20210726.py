# 에리토스테네스의 체 1929번
M,N =map(int, input().split())
sieve = [True] * (N+1)
A = int((N+1)**0.5 +1)
for i in range(2,A):
    if sieve[i] :
        for k in range(i+i,N+1,i):
            sieve[k] = False
for i in range(M,N+1):
    if i >1 and sieve[i]:
        print(i)
