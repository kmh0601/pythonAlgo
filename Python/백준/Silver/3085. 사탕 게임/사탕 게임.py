#BJ3085

N = int(input())
candy = [list(input()) for _ in range(N)]

def checkMaxCandy():
    maxN = 0
    for i in range(N):
        # 행
        cnt = 1
        for j in range(1, N):
            if candy[i][j] == candy[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            maxN = max(cnt, maxN)
        # 열
        cnt = 1
        for j in range(1, N):
            if candy[j][i] == candy[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            maxN = max(cnt, maxN)

    return maxN


result = 1
for i in range(N):
    for j in range(N - 1):
        # 오른쪽 스왑
        if j + 1 < N and candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            result = max(result, checkMaxCandy())
            # 스왑한게 다음 번에 영향을 미치지 않도록 원상복구
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        # 아래쪽 스왑
        if i + 1 < N and candy[i][j] != candy[i + 1][j]:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            result = max(result, checkMaxCandy())
            # 스왑한게 다음 번에 영향을 미치지 않도록 원상복구
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

print(result)
