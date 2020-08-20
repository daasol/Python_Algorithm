n,m,k = map(int, input().split())
data = list(map(int, input().splite()))

data.sort()


result = 0

portion = int(m/(k+1))
reminder = m%(k+1)

result=(data[-1]*k+data[-2])*portion
if reminder!=0 :
    result+=data[-1]*reminder


print(f'결과값 {result}')



