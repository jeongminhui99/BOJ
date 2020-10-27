n = int(input())
f = 0
t = 0
f = n//5 #5kg봉지 개수
b = n%5 #남는 kg

if b != 0: #나누어 떨어지지 않고 나머지가 있는 경우 
    while f >= 0: #5kg개수가 떨어질 때까지
        if b%3 == 0: # 만약 나머지가 3kg로 나누어 떨어진다면 
            t = b//3 # 3kg의 개수 t에 저장
            break # while문 탈출
        f -= 1 # 나머지가 3으로도 안 나우어 질 경우 5kg를 하나 줄인다.
        b += 5 # 하나 줄인것을 나머지에 더한후 다시 3으로 나눈다.

answer = f + t # 5kg과 3kg 개수의 총합 
if answer < 1: #만약 개수가 없으면 -1 출력 / 5와 3의 조합이 안되는 경우
    answer = -1
print(answer)