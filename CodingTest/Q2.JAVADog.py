duration = [1, 2, 1, 4]
dog  = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    }]

def bridge(duration, dog ) :
    #이름만 담는 배열 answer
    answer = [i['이름'] for i in dog]
    for i in dog :
        point = 0
        while point<len(duration)-1 :
            point +=int(i['점프력'])
            duration[point-1]-=int(i['몸무게'])
            if duration[point-1] <0 :
                #지금 i의 '이름'인 곳의 인덱스
                answer[answer.index(i['이름'])]='fail'
                break
    return [i for i in answer if i!= 'fail']

print(f'징검다리 건너기{bridge(duration, dog)}')