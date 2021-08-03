# 3053
import math
R = int(input())
circle1 = R**2 * math.pi
circle2 = (2*R / math.sqrt(2)) **2
print(round(circle1,6))
print(round(circle2,6))


# 9020
sieve = [False,False]+[True]*10000
for i in range(2,101):
    if sieve[i] :
        for k in range(i+i,10001,i):
            sieve[k] = False

T = int(input())
for i in range(T):
    n = int(input())
    A = n//2
    B = A
    for _ in range(10001):
        if sieve[A] and sieve[B]:
            print(A,B)
            break
        A -=1
        B +=1

