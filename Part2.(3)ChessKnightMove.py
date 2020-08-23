location = input()
row = int(location[1])
col = int(ord(location[0]))-int(ord('a'))+1

steps = {
    (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, 2)
}

result = 0

for s in steps :
    nrow = row+s[0]
    ncol = col+s[1]

    #옮긴 위치가 범위 안에 있다면 result증가
    if(1<=nrow<=8 or 1<=ncol<=8) :
        result +=1

print(result)

#for in range에서 리스트의 리스트, 리스트의 튜블인 경우
'''
steps = {
    (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, 2)
}
와 같은 형태로 전체 길이는 8로 반복문을 8번 반복시킨다. 
이 때 for s in range(steps) 

'''