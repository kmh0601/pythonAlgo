# BJ 1283


N = int(input())
shortCut = []

streams = []

for i in range(N):
    streams.append(input().split(" "))

for stream in streams:
    option = True
    # 각 단어의 첫글자가 단축키가 될 수 있는 경우
    for string in stream:
        if option:
            if string[0] in shortCut:
                pass
            else:
                shortCut.append(string[0].upper())
                shortCut.append(string[0].lower())
                # string = "["+string[0]+"]"+string[1:]
                stream[stream.index(string)] = "["+string[0]+"]"+string[1:]
                option = False
    
    # 각 단어의 첫글자가 단축키가 될 수 없는 경우
    if option:
        for string in stream:
            # 이미 단축어가 지정된 경우!
            if option:
                for j in range(len(string)):
                    if string[j] in shortCut:
                        pass
                    else:
                        shortCut.append(string[j].upper())
                        shortCut.append(string[j].lower())
                        #string = string[:j]+"["+string[j]+"]"+string[j+1:]
                        stream[stream.index(string)] = string[:j]+"["+string[j]+"]"+string[j+1:]
                        option = False
                        break
    print(*(stream))