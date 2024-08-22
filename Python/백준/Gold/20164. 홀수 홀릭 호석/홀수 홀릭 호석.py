#BJ 20164

import math

# 자릿수 생각 안하고 계산해야 되니까 문자열로 그냥 받아서 사용~
n = input()

minN = math.inf
maxN = 0


def countOdd(n):
    count = 0
    for i in n:
        if int(i) % 2 != 0:
            count += 1
    return count


def solve(n, odd):
    global maxN, minN
    # 길이가 1이면 그대로 종료
    if len(n) == 1:
        minN = min(minN, odd)
        maxN = max(maxN, odd)
    
    # 길이가 2면 반똥가리
    elif len(n) == 2:
        temp = str(int(n[0]) + int(n[1]))
        solve(temp, odd + countOdd(temp))
    
    # 길이가 3이상이면 이중 리스트로 모든 경우의 수 살펴보기
    else:
        for i in range(len(n) - 2):
            for j in range(i+1, len(n)-1):
                x = n[:i+1]
                y = n[i+1: j+1]
                z = n[j+1:]
                temp = str(int(x) + int(y) + int(z))
                solve(temp, odd + countOdd(temp))

# 재귀로 진행
solve(n, countOdd(n))

print(minN, maxN)