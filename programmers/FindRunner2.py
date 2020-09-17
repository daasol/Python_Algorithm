def solution(participant, completion):
    answer=''
    i=0
    queue=[]
    participant.sort()
    completion.sort()

    while len(completion) :
        com = completion[-1]
        par = participant[-1]

        if com == par :
            completion.pop()
            participant.pop()
        else :
            queue.append(participant.pop())
    answer = queue[-1]
    return answer

participant=['mislav', 'mislav', 'mislav', 'ana', 'mislav', 'mislav', 'stanko']
completion=['stanko', 'ana', 'mislav']

print(solution(participant, completion))