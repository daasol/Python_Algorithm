def solution(board, moves):
    answer = 0
    queue = [0]
    i = 0

    while i < len(moves):
        m = moves[i] - 1
        for j in range(len(board)):
            if board[j][m] > 0:
                queue.append(board[j][m])
                board[j][m] = 0

                if queue[-1] == queue[-2] :
                    queue.pop()
                    queue.pop()
                    answer+=2
                break
        i+=1
    print(answer)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)