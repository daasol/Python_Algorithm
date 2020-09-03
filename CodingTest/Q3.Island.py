import datetime

def solution(standby) :
    #몇 년인지 구하기
    YEAR=0  #1년의 전체 일수
    for i in range(10, 0, -1) :
        year=2**i
        YEAR+=year

    #D_YEAR년 D_MOUNTHd월, D_DATE일, D_DAY에 출발
    date = standby // 1200 #다 태우는데 걸리는 일수
    DATE = date % YEAR  # 탑승 년도에 남은 일수
    D_YEAR = date//YEAR #전체 탑승까지 걸리는 년수
    D_MOUNTH = 0  # 출발 월
    D_DATE=0 #출발 날짜
    D_HOUR = 0
    D_MINIUTE = 0


    # 몇 월인지 구하기
    # 며칠인지 구하기
    mounth,temp = 0,0
    for i in range(10, 0, -1):
        temp=mounth
        mounth += 2 ** i
        D_MOUNTH += 1
        if mounth > DATE:
            D_DATE=DATE-temp
            break

    print(f' D_YEAR : {D_YEAR}, D_DATE : {D_DATE}')

    #몇 시인지 구하기
    rest = standby % 1200
    D_HOUR = (rest // 100) + 9

    #몇 분인지구하기
    depart_minute =[25, 40, 55, 70, 85, 100]
    minute = rest%100 +1
    for i in depart_minute :
       if i > minute :
           D_MINIUTE = depart_minute.index(i)*10
           break

    print(f'D_HOUR :{D_HOUR}, D_MINIUTE : {D_MINIUTE} ')
    #print('f{hour:0>2}:{minute0>2}')


solution(14000605)