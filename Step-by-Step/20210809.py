# 1427
풀이1
import sys
N = list(sys.stdin.readline())
N = N[:len(N)-1]
N.sort(reverse=True)
print("".join(N))

풀이2
nums = input()
N = [int(i) for i in nums]
for i in sorted(N, reverse=True):
    print(i, end="")

# 11650 lambda key 2개 정렬
N = int(input())
result=[]
for i in range(N):
    [a,b] = map(int,input().split())
    result.append([a,b])
result.sort(key = lambda x:(x[0],x[1]))
for i in result:
    print(*i)

# 11651 정렬
N = int(input())
result=[]
for i in range(N):
    [a,b] = map(int,input().split())
    result.append([a,b])
result.sort(key = lambda x:(x[1],x[0]))
for i in result:
    print(*i)

# 1181
N = int(input())
result=[]
for i in range(N):
    a = input()
    result.append(a)
result=list(set(result))
result.sort(key = lambda x:(len(x),x))
for i in result:
    print(i)

# 10814 
N = int(input())
result=[]
for i in range(N):
    [a,b] = input().split()
    result.append([a,b])
result.sort(key= lambda x:int(x[0]))
for i in result:
    print(*i)

# 18870 
import sys
N = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a2 = sorted(list(set(a)))
dic_a2 = {a2[i]:i for i in range(len(a2))}
print(*[dic_a2[i] for i in a])