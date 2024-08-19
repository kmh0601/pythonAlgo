# BJ 1051

N, M = map(int, input().split(" "))

matrix = []

for i in range(N):
    matrix.append(list(map(int, input())))

result = 1

for i in range(N):
    for j in range(M):
        target = matrix[i][j]
        y = j+1
        while y < M:
            if matrix[i][y] == target:
                if i + y - j < N and matrix[i+y-j][j] == target and matrix[i+y-j][y] == target:
                    result = max(result, (y - j + 1)**2)
            y += 1

print(result)