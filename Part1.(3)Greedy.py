#가장 작은 수가 있는 행을 선택할 수 있고, 그 중에서 가장 큰 수를 얻어야 이기는 게임

n, m = map(int, input().split())
result = 0

for i in range(n) :
    data = list(map(int, input().split()))

    min_vaule = min(data)

    result  = max(result, min_vaule)

print(result)

'''
#min과 max 함수를 몰랐을 때
data = list()
min_list = list()

result = 0
for i in range(n) :
    temp = list(map(int, input().split()))
    data.append(temp)


for i in range(n) :
    temp = data[i][0]
    for j in range(m-1) :
        if temp>data[i][j+1] :
            temp =data[i][j+1]
    min_list.append(temp)

min_list.sort()
print(min_list)
result = min_list[-1]



print(f'정답 {result}')
'''