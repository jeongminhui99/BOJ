import sys
x=[]
y=[]
for i in range(3):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)
for i in range(3):
    if x.count(x[i]) == 1:
        a = x[i]
    if y.count(y[i]) == 1:
        b = y[i]
print(a,b)

# x =[]
# y =[]
# for i in range(3):
#     a,b = map(int,input().split())
#     x.append(a)
#     y.append(b)
# x.sort()
# y.sort()
# print(x[0] if x[0] != x[1] else x[2], y[0] if y[0] != y[1] else y[2])