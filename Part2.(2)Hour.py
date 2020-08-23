# 정수 N입력시, N시 59분 59초 까지 3이 한 번이라도 포함되는 경우

n = int(input())
count = 0

for h in range(n+1) :
    for m in range(60) :
        for s in range(60) :
            if '3' in str(h)+str(m)+str(s) :
                count +=1


print(count)
            #두자리수에 3이 들어있는지 어케비교?
