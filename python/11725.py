# 공통된 부모 노드를 찾고 곱하기 10을 하면 됨
# 1에서 1023까지의 자연수가 있는 트리
# 맨 첫 줄에 테스트 케이스 개수

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    while True:
        if a > b:
            a //= 2
        else:
            b //= 2
        if a == b:
            print(a * 10)
            break

