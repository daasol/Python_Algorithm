def solution(numbers):
    answer = []
    i = 0
    while True:
        if i == len(numbers) - 1: break
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
        i += 1
    answer.sort()


    return answer
list  = [2,1,3,4,1]
solution(list)
