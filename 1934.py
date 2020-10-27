t=int(input())
for i in range(t):
    a,b=map(int, input().split())
    r = a*b
    while b: #b가 0이 될때 최대공약수는 a
        a, b = b, a%b
    r = r // a #최소공배수는 A=r(gcd)*a , B=r*b 일때 AB // r(gcd) 하면 구할 수 있다.
    print(r)


