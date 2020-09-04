
def solution(page, num) :
    chair = []*num
    answer = 0


    for i in page :
        if len(chair)<3 :
        #자리가 남아있는 경우
            #동종이 있는 경우
            if i in chair :
                '''
                항상 0번째 값을 pop한다는 전제가 깔린 경우이기 때문에 올바르지 않음
                hit되는 페이지는 1번째 혹은 두번째 일 수도 있다. 
                chair.append(chair.pop(0))
                '''
                #동종이 첫 번째가 아니라, 두번째 혹은 세번쩨에 있는 경우 동종을 찾아 pop하고, append해줌
                hit = chair.pop(chair.index(i))
                chair.append(hit)
                answer +=1
            else :
            #이동이 들어온 경우
                chair.append(i)
                answer+=60
        else :
        #자리가 모두 찬 경우
        #동종이있는경우
            if i in chair:
                chair.append(chair.pop(0))
                answer += 1
            else:
                # 이동이 들어온 경우
                #이종일 경우 동종을 찾아 pop할 필요가 없음.
                chair.pop(0)
                chair.append(i)
                answer += 60
    return f'{answer//60}분 {answer%60}초'

page = ['척추동물', '어류', '척추동물',
        '무척추동물', '파충류', '척추동물',
        '어류', '파충류']
print(solution(page, 3))