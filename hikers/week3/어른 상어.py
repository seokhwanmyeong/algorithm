import sys

sys.stdin = open('dev/stdin', 'r')
# input = sys.stdin.readline

#주어진 값 n,m,k
n, m, k = map(int, input().split())

#input 배열을 담을 board, 상어번호순(index기준)으로 좌표, 방향을 담을 배열
board, shark = [], [[]for _ in range(m)]

for i in range(n):
    #들어오는 input을 board에 담기
    board.append(list(map(int, input().split())))
    for j in range(n):
        # 해당보드에 상어가 있을경우,
        # 1. shark배열에 해당 좌표를 담고
        # 2. 상어번호와 향기 k값을 배열로 저장
        if board[i][j]:
            shark[board[i][j] - 1].extend([i,j])
            board[i][j] = [board[i][j], k]

# 상어가 처음 바라보는 방향값(input)
base_d = list(map(int, input().split()))
for i in range(m):
    shark[i].append(base_d[i]) #상어별로 처음 바라보는 방향 삽입

# 상어의 우선순위별 주어지는 방향값
# 4가지 방향에 각각 4가지 순서를 shark_d에 저장
shark_d = [[] for _ in range(m)]
idx = -1
for i in range(4*m):
    # i가 0일경우, idx += 1이 실행되기때문에 -1로 기본설정
    if i % 4 == 0:
        idx += 1
    shark_d[idx].append(list(map(int, input().split())))

answer = 0
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

while True:
    answer += 1
    # 1000 초과일 경우 break
    if answer == 1001:
        print(-1)
        break

    #이동한 좌표를 담을 배열
    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        if shark[i] != 0:
            # 해당 상어의 좌표값, 방향, 해당조건 검사를 위한 p값 할당
            x, y, d, p = shark[i][0], shark[i][1], shark[i][2], 0

            # 1. 영역냄새가 없는 조건
            for j in range(4):
                nd = shark_d[i][d-1][j] #우선순위 방향값 추출
                nx, ny = x + dx[nd], y + dy[nd] #우선순위 방향값 할당
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 0:
                        p = 1
                        break
            
            # 2. 영역냄새가 없는 조건을 통과하지 못한 경우, p=0으로 존재
            #    자기 족적으로 회귀조건
            if p == 0:
                for j in range(4):
                    nd = shark_d[i][d-1][j]
                    nx, ny = x + dx[nd], y + dy[nd]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny][0] == i+1:
                            break

            # 상어 이동좌표를 check배열에 할당 및 강함순서비교
            if check[nx][ny]:
                if check[nx][ny] < i+1: shark[i] = 0
                else: shark[check[nx][ny]-1] = 0
            else:
                check[nx][ny] = i+1
                shark[i] = [nx, ny, nd]

    # board의 상어의 k값들을 감소
    # 0일 시, 해당좌표는 0으로 초기화
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = 0

    #이동한 상어들의 새로운 좌표 및 k값 할당
    for i in range(m):
        if shark[i]:
            x, y = shark[i][0], shark[i][1]
            board[x][y] = [i+1, k]


    # 제외된 상어는 0값
    # 0의 개수 = 1번을 제외한 상어마리면 answer을 print
    if shark.count(0) == m-1:
        print(answer)
        break