# BJ12865

N, K = map(int, input().split(" "))

# [[w,v], [w,v], ...]
items = [[0,0]]

for _ in range(N):
    items.append(list(map(int,input().split(" "))))

items.sort()

# [[무게 K] * 갯수 N]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        w,v = items[i]
        if i == 0 or j == 0:
            pass 
        elif w <= j:
            # 집어넣거나 or 집어넣지 않거나
            # 이때, 집어넣지 않는다 == dp[i-1][j]
            # 이때, 집어넣는다  == dp[i-1][j-w] + v
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])