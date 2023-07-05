def solution(n):
    tri = [[0] * n for _ in range(n)]
    arr = []
    # tri 인덱스 초기화
    x, y = -1, 0
    # tri 리스트에 저장할 숫자
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            # 값 할당 후 1 증가
            tri[x][y] = num
            num += 1

    for i in tri:
        for j in i:
            if j != 0:
                arr.append(j)

    return arr