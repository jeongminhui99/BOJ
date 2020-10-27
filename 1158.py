n, k = map(int, input().split())
list = [i for i in range(1,n+1)]
new = [] #답
index = 0
for j in range(n):
    index += k-1
    if index >= len(list):
        index %= len(list)
    new.append(list.pop(index))
print("<", end='')
for i in new:
    if i == new[-1]:
        print(i, end = '')
    else:
        print("%s, " %(i), end='')
print(">")

# 큐 이용하기
# import collections
# n, k = map(int, input().split())
# result=[]
# queue = collections.deque([i for i in range(1, n+1)]) #deque만들고 큐 구현
# #deque는 스택과 큐의 기능을 모두 가진 객체로 출입구를 양쪽에 가지고 있다. 
# #스택 : append(), pop() / 큐 : appendleft(), pop(), append(), popleft()
# while len(queue) > 0:
#     for _ in range(k):
#         if _ == k-1:
#             num = queue.popleft()
#             result.append(num)
#         else:
#             num = queue.popleft()
#             queue.append(num)

# print("<" + ", ".join(list(map(str,result))) + ">") #join함수