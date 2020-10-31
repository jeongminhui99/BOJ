import sys
import math
def prime(n):
    if(n<2):
        return False
    for i in range(2, n) :
        if n%i == 0:
            return False
    return True
n = int(sys.stdin.readline())
n_list = list(map(int, input().split()))
cnt=0   
for i in n_list:
    if prime(i) == True:
        cnt += 1
print(cnt)
# n = int(sys.stdin.readline())
# n_list = list(map(int, input().split()))
# cnt = 0
# for i in n_list:
#     if i==2:
#         cnt += 1
#     for k in range(2,i):
#         if i%k == 0:
#             break
#         else:
#             if k == i-1:
#                 cnt += 1
# print(cnt)   