n = int(input())
coin = [500, 100, 50, 10, 5, 1]
count = 0
n = 1000 - n

for i in coin:
    count += n//i   # //연산자 : 정수형 좌항을 우항으로 나눔 (몫)
    n %= i
print(count)
