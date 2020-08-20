n, m, k = map(int, input().split())
data = list(map(int, input().split()))


data.sort()
MMax = data[-1]
SMax = data[-2]
result = 0

while True :
    for i in range(k) :
        if(m==0) : break
        result +=MMax
        m-=1

    if(m==0) :break
    result+=SMax
    m-=1

    if(m==0) : break


print(f'결과값 {result}')

