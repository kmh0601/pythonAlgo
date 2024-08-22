# BJ 17276

from copy import deepcopy

T = int(input())

for t in range(T):  
    N, rotate = map(int, input().split())

    # 새로운 표현!
    arr = [list(map(int, input().split())) for _ in range(N)]  

    result = [[0]*N for _ in range(N)]
  
    if rotate < 0:  
        rotate = 360 + rotate  
    # 제자리 일 경우 그대로 출력  
    if rotate == 360 or rotate == 0:  
        for tmp in arr:  
            print(*tmp)  
    else:  
        # 45의 배수만큼 반복  
        for _ in range(rotate//45):  
            for i in range(N):  
                for j in range(N):
                    # 무한 조건
                    if i==j:  
                        result[i][j] = arr[N//2][j]  
                    elif i == N//2:  
                        result[i][j] = arr[N-j-1][j]                  
                    elif i+j == N-1:  
                        result[i][j] = arr[i][N//2]  
                    elif j == N//2:  
                        result[i][j] = arr[i][i]  
                    # 나머지는 그대로 반영
                    else:  
                        result[i][j] = arr[i][j]  
            arr = deepcopy(result)
  
        for tmp in result:  
            print(*tmp)