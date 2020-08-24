from collections import deque

n, m = map(int, input().split())

dx = (-4, 0, 4, 0)
dy = (0, -1, 0, 1)

array = []
for _ in range(n) :
    array.append(list(map(int, input())))

def dfs(x, y) :
    if x<=-1 or x>=n or y<=-1 or y>=m :
        #범위를 벗어나면 즉시종료
        return False

    if array[x][y]==0 :
        #방문처리
        array[x][y]=1
        '''
        상하좌우 4방향을 재귀함수로 탐색하고
        방문할 수 있는 곳이면 방문한다.
        이렇게 하면 처음 재귀함수가 시작된 x,y값에서 출발하여 연결된 모든 곳을 탐색하고 
        result를 하나로 퉁쳐줌 (연결된 여러 0들을 하나로 묶어줌
        
        '''
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)


        return True

    return False



result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            result+=1

print(result)
