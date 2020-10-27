import sys
input = sys.stdin.readline
#답은 나오지만 시간초과
# k=int(input())
# n=list(map(int, input().split()))
# aa=[-1 for _ in range(k)] # [-1,-1,-1....]
# for j in range(len(n)):
#     i=0
#     for k in range(j+1,len(n)):
#         if n[j] < n[k]:
#             index=k
#             i = 1
#             break
#     if i != 0:
#         aa[j] = n[index]
# for i in range(len(aa)):
#     print(aa[i], end = ' ')

k=int(input())
n=list(map(int, input().split()))
stack = [] #인덱스 저장할 공간
aa=[-1 for _ in range(k)] # [-1,-1,-1....]
stack.append(0) # 첫번째 인덱스 0 저장
i=1 #첫번째 인덱스 값이랑 비교할 인덱스 
while stack and i<k: #i가 k-1까지 k는 비교할께 없음
    while stack and n[stack[-1]] < n[i]:
        aa[stack[-1]] = n[i]
        stack.pop() #aa에 값이 생긴 인덱스는 pop하고 아직 해당 인덱스 값이 없는 것만 넣어둔다.
    stack.append(i)
    i += 1
for i in range(k): 
    print(aa[i], end = " ")



