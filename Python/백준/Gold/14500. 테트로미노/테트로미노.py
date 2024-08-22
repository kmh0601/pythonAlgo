# BJ14500

N, M = map(int, input().split(" "))

matrix = [list(map(int,input().split(" "))) for _ in range(N)]

# 긴 모양 체크
def lCheck():
    count = 0
    for i in range(N):
        for j in range(M):
            # ㅣ
            if j + 3 < M:
                tempX = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3]
            else:
                tempX = 0
            # -
            if i + 3 < N:
                tempY = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
            else:
                tempY = 0
            
            count = max(count,tempX, tempY)
    return count

# 지그재그 모양
def zigzagCheck():
    count = 0
    for i in range(N):
        for j in range(M):
            # --    &     -- 
            #   --  &  --
            if j + 2 < M and i + 1 < N:
                temp1 = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j+2]
                temp2 = matrix[i+1][j] + matrix[i+1][j+1] + matrix[i][j+1] + matrix[i][j+2]
            else:
                temp1 = temp2 = 0
            # ㅣ     &      ㅣ
            # ㅣ ㅣ       ㅣ ㅣ
            #   ㅣ   &   ㅣ
            if j + 1 < M and i + 2 < N:
                temp3 = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1]
                temp4 = matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j]
            else:
                temp3 = temp4 = 0
            
            count = max(count,temp1,temp2,temp3,temp4)
    return count

# ㅗ 모양
def fyCheck():
    count = 0
    for i in range(N):
        for j in range(M):
            # ㅗ
            # ㅜ
            if i + 1 < N and j + 2 < M :
                temp1 = matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i][j+1]
                temp2 = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1]
            else:
                temp1 = temp2 = 0
            # ㅏ
            # ㅓ
            if i + 2 < N and j + 1 < M :
                temp3 = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+1][j+1]
                temp4 = matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i+1][j]
            else: 
                temp3 = temp4 = 0
        
            count = max(count,temp1,temp2,temp3,temp4)
    
    return count

# ㅁ 모양
def boxCheck():
    count = 0
    for i in range(N):
        for j in range(M):
            if j + 1 < M and i + 1 < N:
                tempX = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            else:
                tempX = 0
            
            count = max(count,tempX)
    return count

# L 모양
def LCheck():
    count = 0
    for i in range(N):
        for j in range(M):
            # ㅣ ㅣ  &   ㅣ ㅣ
            # ㅣ           ㅣ
            # ㅣ    &      ㅣ

            # ㅣ     &      ㅣ
            # ㅣ            ㅣ
            # ㅣ ㅣ   &  ㅣ  ㅣ
            if i + 2 < N and j + 1 < M:
                temp1 = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i][j+1]
                temp2 = matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i][j+1]
                temp3 = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1]
                temp4 = matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i+2][j]
            else: 
                temp1= temp2 = temp3 = temp4 = 0
            # ㅣ ㅣ ㅣ   &   ㅣ ㅣ ㅣ
            # ㅣ                 ㅣ

            # ㅣ        &        ㅣ    
            # ㅣ ㅣ ㅣ       ㅣ ㅣ ㅣ
            if i + 1 < N and j + 2 < M:
                temp5 = matrix[i][j] + matrix[i+1][j] + matrix[i][j+1] + matrix[i][j+2]
                temp6 = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+2]
                temp7 = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2]
                temp8 = matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2]
            else:
                temp5 = temp6 = temp7 = temp8 = 0
            count = max(count,temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8)
    
    return count


result = max(lCheck(), fyCheck(), zigzagCheck(), LCheck(), boxCheck())

print(result)
    