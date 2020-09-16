def solution(board, moves):
    answer = 0

    for i in board:
        for j in i:
            if j > 0:
                top = j
                if len(moves)==0 :
                    moves.append(top)
                elif (top == moves[-1]):
                    answer += 1
                    moves.pop()
                else:
                    moves.append(top)

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = []
solution(board, moves)
