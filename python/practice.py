# 큰 수의 법칙
# 첫째 줄에 n, m, k의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 n개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
# 입력으로 주어지는 k는 항상 m보다 작거나 같다.
# 첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.

# n,m,k = map(int, input().split())
# data=list(map(int,input().split()))

n = int(input())
coin = [500, 100, 50, 10, 5, 1]
count = 0
n = 1000 - n

for i in coin:
    count += n//i   # //연산자 : 정수형 좌항을 우항으로 나눔 (몫)
    n %= i
print(count)





