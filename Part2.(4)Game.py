n, m = map(int, input().split())
row, col, dir = map(int, input().split())
array=[]
for i in range(n) :
    array.append(list(map(int, input().split())))

#dx,dy 접근할때 함수로 접근하면 안되고, 2차원 배열로 접근해야됨 (x,y)순서가 아니라 (y,x) -> dy,dx
# 북 동 남 서
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

check = [[0]*m for _ in range(n)]
check[row][col]=1

def turn_left() :
    global dir
    dir-=1
    if(dir==-1) : dir=3

count = 1
turn_time=0

while True :
    turn_left()
    nx = row + dx[dir]
    ny = col + dy[dir]

    #갈 수 있는 경우
    if(check[nx][ny]==0 and array[nx][ny]==0) :
        row = nx
        col = ny
        count+=1
        check[row][col]=1
        # 한 번 이동했으므로, 방향을 돌 수 있는 기회가 4번 다시 생김
        turn_time = 0
        
        continue

    # 바다이거나 갔던 곳인 경우
    else :
        turn_time+=1

    if turn_time==4 :
        #한 바퀴 돌아 다시 원래 방향으로 복귀한 경우
        nx = row-dx[dir]
        ny = col-dy[dir]
        #다시 원래로 돌아감
        if(array[nx][ny]==0) :
            row=nx
            col=ny
        #바다로 막혀있는 경우 돌기만함
        else :
            break
        turn_time=0

print(count)





'''
#맵 크기
n, m = map(int, input().split())

row, col, dir = map(int, input().split())

check=[[0]*m for _ in range(n)]
check[row][col]=1 #현재 좌표 방문처리

array=[]
for i in range(n) :
    array.append(list(map(int, input().split())))

#0 : 북쪽보고있을 때 서쪽으로 이동은 -1, 0
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def left_turn() :
    #왼족으로 회전 : 0->3->2->1 순으로 회전
    #0->3으로갈때 -1이 나오면 서쪽으로 회전
    global dir
    dir-=1
    if(dir==-1) : dir=3
    print(dir)

count =1
turn_time = 0

while True :
        left_turn()
        nx = row+dx[dir]
        ny = col+dy[dir]

        #회전한 후, 가보지 않은 칸이 존재하는 경우
        if(check[nx][ny]==0 and array[nx][ny]==0) :
            check[nx][ny]=1
            row=nx
            col=ny
            count+=1
            turn_time=0
            continue

        #회전한 후, 가보지 않은 칸이 없거나 바다인경우
        else :
            turn_time+=1

        #4방향 모두 이동불가
        if turn_time==4 :
            nx=row-dx[dir]
            ny=col-dy[dir]
            #뒤로갈 수 있다면 이동하기
            if(array[nx][ny]==0) :
                row=nx
                col=ny
            #바다로 막혀있는 경우
            else :
                break
            turn_time=0


print(f'결과{count}')

'''

