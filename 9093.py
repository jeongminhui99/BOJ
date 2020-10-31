# n = int(input())
# for i in range(n):
#     s = list(map(str, input().split()))
#     for j in s:
#         for k in range(len(j)):
#             print(j[len(j)-1-k], end='')
#         print(end=' ')

import sys
n = int(input())
s = sys.stdin.read().splitlines() # ['I love upi', 'djfkdf dfdj'] ^z누를 때까지 입력받는다.
res = []
for idx in range(n):
    res.append(" ".join([i[::-1] for i in s[idx].split()]))
print("\n".join(res))