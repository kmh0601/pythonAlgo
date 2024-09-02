#BJ11053

N = int(input())

stream = list(map(int,input().split(" ")))

dp = [1 for _ in range(N)]

for i in range(0, N):
    for j in range(0, i):
        if stream[i] > stream[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))