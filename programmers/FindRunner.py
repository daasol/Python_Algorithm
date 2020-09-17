def solution(participant, completion):
    answer = ''
    queue = []

    while len(completion) :
        com = completion.pop()
        if com in participant :
            participant.remove(com)


    while len(participant) :
        answer = participant.pop()
    return answer

participant=['mislav', 'stanko', 'mislav', 'ana']
completion=['stanko', 'ana', 'mislav']

print(solution(participant, completion))