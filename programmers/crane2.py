def solution(board, moves):
    answer = 0
    queue = [0]
    top=0
    i = 0
    top = queue[0]
    while i < len(moves):
        m = moves[i] - 1
        for j in range(len(board)):
            if board[j][m] > 0:
                if top == board[j][m] :
                    queue.pop()
                    answer+=2
                    top = queue[-1]

                else :
                    queue.append(board[j][m])
                    top = queue[-1]
                board[j][m] = 0
                break
        i+=1
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)