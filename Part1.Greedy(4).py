#N이 1외되는 최소횟수 구하기

n, k = map(int, input().split())
count = 0

while True :
    if(n%k==0) :
        n=n//k
    else :
        if (n == 2 % k == 2):
            count += 1
            break
        n-=1

    count += 1
    if (n == 1): break

print(count)







