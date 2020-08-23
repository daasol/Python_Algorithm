#상하좌오 이동하기 : map을 벗어나는 범위는 이동하지 않음
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1] #좌우
dy = [-1, 1, 0, 0] #상하
move_types=['L', 'R', 'U', 'D']

for plan in plans :
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x+dx[i]

            ny = y+dy[i]

    if nx<1 or ny<1 or nx>n or ny>n :
        continue
    x, y =nx, ny

print(x, y)







'''
n = int(input())
direction = list(input().split())

data = [[0]*n for _ in range(n)]
print(direction)
print(data)
i, j = 0, 0
for l in range(len(direction)) :
    if ((direction[l] == 'R') & (j<n-1)):
        j += 1

    elif ((direction[l] == 'L') & (0<j)):
        j -= 1

    elif ((direction[l] == 'U') & (0<i)):
        i -= 1

    elif ((direction[l] == 'D') & (i<n-1)):
        i += 1
    else :
        continue

print(f'현재 위치{i+1}, {j+1}')

'''





