def solution(participant, completion):
    answer = ''
    i = 0
    queue = []
    participant.sort()
    completion.sort()

    while len(completion):
        com = completion[-1]
        par = participant[-1]

        if com == par:
            completion.pop()
            participant.pop()
        else:
            answer = participant.pop()
    return answer
