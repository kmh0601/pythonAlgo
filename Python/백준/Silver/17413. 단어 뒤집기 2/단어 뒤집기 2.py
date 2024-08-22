# BJ 17413

S = input()
result = []

i = 0
while i < len(S):
    if S[i] == '<':
        temp = ""
        while S[i] != '>':
            temp += S[i]
            i += 1
        temp+=">"
        i += 1
        result.append(temp)
    else:
        temp = ""
        while i < len(S) and S[i] != '<':
            if S[i] == " ":
                i += 1
                break
            temp+=S[i]
            i += 1
        result.append(temp[::-1])

for i in range(len(result)):
    if '<' in result[i] or (i+1 < len(result) and '<' in result[i+1]):
        print(result[i], end="")
    else:
        print(result[i], end=" ")