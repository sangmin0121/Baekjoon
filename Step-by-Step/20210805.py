# # 2750 삽입정렬 O(N^2)
N = int(input())
result = []
for i in range(N):
    A = int(input())
    result.append(A)
for end in range(len(result)):  
    for i in range(end,0,-1):
        if result[i-1] > result[i] :
            result[i-1], result[i] = result[i], result[i-1]
for i in result:
    print(i)


# 2751 병합정렬 O(nlogn)
# 참고사이트 : https://eunhee-programming.tistory.com/105
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0
    arr=[]
    print(left)
    # print(right)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    arr += left[i:]
    arr += right[j:]

    return arr

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr = merge_sort(arr)

for i in arr:
    print(i)

# 10989 카운팅정렬 O(n+k)
import sys
N = int(sys.stdin.readline())
a = [0 for _ in range(10001)]
for i in range(N):
    num =int(sys.stdin.readline())
    a[num] +=1
for i in range(1,10001):
    count=a[i]
    for k in range(count):
        print(i)
