def gcd(a,b): # 최대공약수 구하는 함수
    if b==0:
        return a
    return gcd(b, a%b) # b가 a보다 더 커도 b가 a위치로 오면서 큰 수가 앞으로 온다.

n = int(input())
for i in range(n):
    sum = 0
    num = list(map(int, input().split()))
    for j in range(1,len(num)-1): # 첫 번째 원소는 입력할 수의 개수이므로 1부터
        for k in range(j+1,len(num)):
            sum += gcd(num[j],num[k]) #1은 제외
    print(sum)

# import sys
# import itertools
# input = sys.stdin.readline
# t = int(input())
# for i in range(t):
#     num_list = list(map(int, input().split()))
#     num_list = num_list[1:]
#     ans = 0
#     for a, b in itertools.combinations(num_list, 2): #중복 포함 안함
#         ans += gcd(a, b)
#     print(ans)