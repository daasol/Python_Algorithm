from collections import deque

def solution(page) :
    minute, second =0, 0
    queue=deque()
    chair = {}
    count=0

    for i in page :
        #자리에 동종이 있을 때 무릎에 앉음
        if i in chair :
            #동종 무릎에는 count를 세지 않는다.
            chair[i] +=1
            queue.popleft()
            queue.append(i)
            second+=1

        #자리가 꽉차있을 때
        elif count>=3 :
            key, value = queue.popleft()
            del(chair[key])
            queue.append(i)
            chair[i] = 1
            minute+=1

        else :
            #자리에 동종이 없을 때
            chair[i]=1
            queue.append(i)
            count+=1
            minute += 1

    print(f'count : {count}, :: {chair}')
    print(f'{minute}분 {second}초')

page = ['척추동물', '어류', '척추동물',
        '무척추동물', '파충류', '척추동물',
        '어류', '파충류']
solution(page)