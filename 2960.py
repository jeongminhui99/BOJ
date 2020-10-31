n, k = map(int,input().split())
n_list = [False,False]+[True for i in range(2,n+1)]
a_list = []
for i in range(2, n+1):
    if n_list[i]:
        a_list.append(i)
        for j in range(i*2, n+1, i):
            n_list[j] = False
            if j not in a_list:
                a_list.append(j)
print(a_list[k-1])