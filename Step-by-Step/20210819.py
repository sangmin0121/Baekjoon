# # 2753
# a = int(input())
# if a % 4 == 0 and (a % 100 !=0 or a % 400 ==0) :
#     print(1)
# else:
#     print(0)

# # 2562
# result = []
# for i in range(9):
#     result.append(int(input()))
# print(max(result))
# print(result.index(max(result))+1)

# # 3052
# answer = [int(input()) for _ in range(10)]
# answer = [i%42 for i in answer]
# print(len(set(answer)))


# # 1181번
# num = int(input())
# answer = []
# for i in range(num):
#     string = input()
#     answer.append(string)
# answer = list(set(answer))
# answer.sort(key = lambda x :(len(x),x))
# for i in answer:
#     print(i)

# # 1546
# num = int(input())
# answer = list(map(int,input().split()))
# answer = [i*100/max(answer) for i in answer]
# print(sum(answer)/num)

# # 4344
# case_num = int(input())
# for i in range(case_num):
#     case = list(map(int,input().split()))
#     case_avg = sum(case[1:])/case[0]
#     result = list(filter(lambda x:x > case_avg , case[1:]))
#     print("{0:.3f}%".format(round(len(result)/case[0]*100,3)))

# # 11720
# n = int(input())
# a = list(map(int,input()))
# print(sum(a))

# # 15649 DFS
# N,M = map(int,input().split())

# s = []

# def dfs():
#     if len(s) == M:
#         print(" ".join(map(str,s)))
#         return
    
#     for i in range(1,N+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()
# dfs()

# 15650 DFS2

N, M = map(int,input().split())

s = []

def dfs(start):
    if len(s) == M:
        print(" ".join(map(str,s)))
        return
    for i in range(start,N+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)