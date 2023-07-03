# 아기 상어

from collections import deque
INF = 1e9

# 공간의 크기 입력 받음
n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 아기상어 현재 크기
shark_size = 2
# 아기상어 현재 위치
shark_x, shark_y = 0, 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            shark_x, shark_y = i, j
            array[shark_x][shark_y] = 0

dx = [-1, 0, 1, 0] # 좌 상 우 하
dy = [0, 1, 0, -1]

# 모든 위치의 최단 거리만 계산하는 BFS 함수
def bfs():
    # 값이 -1 이면 도달할 수 없음 : 초기화
    dist = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보고, 거리 0
    q = deque([(shark_x, shark_y)])
    dist[shark_x][shark_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # 크기가 자기보다 작거나 같은 경우에 지나갈 수 있음
                if array[nx][ny] <= shark_size and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    # 모든 위치까지의 최단 거리 테이블 반환
    return dist

# 최단 거리 테이블 주어졌을 떄, 먹을 물고기 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 경우
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < shark_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    # 먹을 수 있는 물고기가 없는 경우
    if min_dist == INF:
        return None
    else:
        # 먹을 물고기의 위치와 최단 거리
        return x, y, min_dist

# 최종 답
result = 0
# 현재 크기에서 먹은 양
ate = 0

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        shark_x, shark_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에 0이 오도록
        array[shark_x][shark_y] = 0
        ate += 1
        # 현재 크기 이상으로 먹을 시, 크기 증가
        if ate >= shark_size:
            shark_size += 1
            ate = 0