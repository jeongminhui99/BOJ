# n = list(bin(int(input()))[2:])
# n2 = list(reversed(n)) #리스트 역순 정렬
# sum = 0
# for i in range(len(n2)):
#     sum += (2**(len(n2)-1-i))*int(n2[i])
# print(sum)

n = bin(int(input()))[2:]   # 2 진수로 만들어 주는 bin
print(int(n[::-1],2))       # 이걸 다시 10진수로 만들어 줄 때