# BJ17626
import math

N = int(input())

dp = [False for _ in range(N+1)]

for i in range(1, int(N**(1/2)+1)):
    dp[i**2] = 1

def FourSquares(n):
    if dp[n] or n == 0:
        pass
    else:
        x = int(n ** (1/2))
        dp[n] = math.inf
        for i in range(x, x//2 - 1, -1):
            dp[n] = min(FourSquares(n-(i**2)) + 1, dp[n])
    return dp[n]

print(FourSquares(N))