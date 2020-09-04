from collections import deque

def solution(page) :
    time = 0
    queue=deque()
    chair = {}
    count=0

    for i in page :
        #자리에 동종이 있을 때 무릎에 앉음
        if i in chair :
            #동종을 queue에서 빼내야하는데, 나는 첫 번째를 pop으로 전제하고 있음...
            
            chair[i] +=1
            queue.popleft()
            queue.append(i)
            time+=1

        #자리가 꽉차있을 때
        elif count>=3 :
            key = queue.popleft()
            del(chair[key])
            queue.append(i)
            chair[i] = 1
            time+=60

        else :
            #자리에 동종이 없을 때
            chair[i]=1
            queue.append(i)
            count+=1
            time+=60

    print(f'count : {count} :: {chair}')
    print(f'{time//60}분 {time%60}초')

page = ['척추동물', '어류', '척추동물',
        '무척추동물', '파충류', '척추동물',
        '어류', '파충류']
solution(page)