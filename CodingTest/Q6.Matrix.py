import numpy as np


def solution(first, second) :
    answer = []
    #second array를 1회선 시키고, first와 더함
    np.rot90(second, 1) + np.array(first)

    #first에 second를 1회전 시킨 배열을 뺌
    np.array(first) - np.rot90(second, 1)
    result = np.rot90(second, 1)+ np.array(first)


    #result의 0번째 행을 answer에 담는다.
    for i in result[0] :
        answer.append(str(i))

    #문자열 ' '의 공백을 없앤다.
    answer=''.join(answer)

    #정수형, 8진법으로 형변환 int(str, n) : str을 n진법으로
    answer = (int(answer, 8))

    print(answer)
    for k in range(5) :
        print(chr(int(''.join([str(i) for i in result[k]]), 8)))







first = [
[1, 0, 0, 0, 0],
[0, 0, 1, 0, 1],
[0, 0, 1, 0, 1],
[0, 0, 1, 0, 1],
[0, 0, 1, 0, 1]
]

second = [
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 3],
[0, 0, 0, 0, 4],
[0, 2, 0, 0, 2],
[4, 5, 0, 2, 0]
]

solution(first, second)