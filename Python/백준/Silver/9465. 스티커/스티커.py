T = int(input())

for _ in range(T):
    N = int(input())
    dp = [[0 for _ in range(N)] for _ in range(2)]
    n = []
    for _ in range(2):
        a = list(map(int,input().split()))
        n.append(a)

    for j in range(N):
        for i in range(2):
            # 첫째 행의 경우
            if i == 0:
                # 왼쪽이 존재하는 경우
                if j == 1:
                    dp[i][j] = dp[i+1][j - 1] + n[i][j] # 전칸에서 오는 경우
                if j == 0:
                    dp[i][j] = n[i][j]
                else:
                    dp[i][j] = max(dp[i+1][j - 1] + n[i][j], dp[i+1][j-2]+n[i][j]) # 전전칸에서 오는 경우

            # 둘째 행의 경우
            else:
                # 왼쪽이 존재하는 경우
                if j == 1:
                    dp[i][j] = dp[i-1][j - 1] + n[i][j] # 전칸에서 오는 경우
                elif j == 0 :
                    dp[i][j] = n[i][j]
                else:
                    dp[i][j] = max(dp[i-1][j - 1] + n[i][j], dp[i-1][j-2]+n[i][j]) # 전전칸에서 오는 경우

    print(max(max(dp[0]),max(dp[1])))


'''
결국 0행에서 하나 골랐으면 1행에서 하나 고르는 형식
이때 i 열에 도달하려면 i-1 에서 오거나 i-2 에서 오는 방식 둘 중에 하나다.(i-3 의 경우에는 같은 행에서 하나를 더 택할 수 있었으므로
고려할 대상이 아니다.)
'''