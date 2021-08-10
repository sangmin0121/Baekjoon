# 2108 Counter 클래스
from collections import Counter
import sys
T = int(sys.stdin.readline())
answer = []
for i in range(T):
    answer.append(int(sys.stdin.readline()))
answer.sort()   # 오름차순으로 해야 두 번째 작은 수 찾기 용이

print(round(sum(answer)/T))
print(answer[T//2])

cnt = Counter(answer).most_common(2)  # 빈도수 뽑기 + 상위 몇개까지 값
if len(answer) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(answer)-min(answer))