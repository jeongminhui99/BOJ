n_list = [False,False]+[True for i in range(2,1000001)]
for i in range(2, 1000001):
    if n_list[i]:
        for j in range(i*2, 1000001, i):
            n_list[j] = False
            
n, m = map(int,input().split())
for i in range(n,m+1):
    if n_list[i]:
        print(i)