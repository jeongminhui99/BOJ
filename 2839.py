n = int(input())
f = 0
t = 0

f = n//5 
b = n%5

if b != 0:
    while f >= 0:
        if b%3 == 0:
            t = b//3
            break
        f -= 1
        b += 5

answer = f + t
if answer < 1:
    answer = -1
print(answer)