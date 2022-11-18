#1 is red
#2 is black
import copy
def expand(int_board):#returns an array were each slot represents a
    board_state=format(int_board,'063b')
    i=0
    j=0
    filled=["" for x in range(7)]
    while i <= 54:
        filled[j]=board_state[i:i+9]
        j=j+1
        i=i+9

    return filled

def extra_expand(coloumns):
    board=[
        #0,1,2,3,4,5,6
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    i=0
    for coloumn in coloumns:
        #print("!!!!!!!!!!!!in fIRST FOR!!!!!!!!!!")
        #print(coloumn)
        first_empty=coloumn[0:3]
        #f_empty is index
        f_empty=int(first_empty,2)
        #print(f_empty)
        filled=6-f_empty
        last_bit=9

        if filled != 0:
            #print("!!!!!!!!!!!!CHECK DONE!!!!!!!!!!")
            for j in range(5,f_empty-1,-1):
                #print("!!!!!!!!!!!!in SECOND FOR!!!!!!!!!!")
                if(coloumn[last_bit-1]=='1'):
                    #print("it is 1")
                    board[j][i]=1
                else:
                    #print("it is 2")
                    board[j][i]=2
                last_bit=last_bit-1
        i=i+1
        #print(i)
    return board

def compress(board):
    filled=["" for x in range(7)]
    for i in range(6,-1,-1):
        col_position = 0
        for j in range(5,-1,-1):
            if j==0:
                if board[j][i] == 0:
                    col_position = j + 1
                    if filled[i] != "":
                        col_position = format(col_position, '03b')
                        filled[i] = format(int(filled[i], 2), '06b')
                        filled[i] = col_position + filled[i]
                    else:
                        filled[i] = format(col_position, '03b') + '000000'

                    break
                elif board[j][i] == 1:
                    filled[i] = format(0, '03b') + format(1, "01b") + filled[i]
                elif board[j][i] == 2:
                    filled[i] = format(0, '03b') + format(0, "01b") + filled[i]

            elif board[j][i] == 0:
                col_position=j+1
                if filled[i] != "":
                    col_position = format(col_position, '03b')
                    filled[i]=format(int(filled[i],2),'06b')
                    filled[i]=col_position+filled[i]
                else:
                    filled[i]=format(col_position,'03b')+'000000'
                break
            elif board[j][i] == 1:
                filled[i]=format(1,"01b")+filled[i]
            elif board[j][i] == 2:
                filled[i]=format(0,"01b")+filled[i]


    return filled

def extra_compress(board):
    filled=compress(board)
    temp=''
    for f in filled:
        temp=temp+f
    int_board=int(temp,2)
    return int_board

def place(int_board,col): #the coloum where the player wants to add a piece
    coloums=expand(int_board)
    coloum=coloums[col]
    first_empty=coloum[0:3]
    f_empty=int()

def is_goal(board):
    for i in range(6):
        for j in range(7):
            if board[i][j] == 0:
                return False
    return True


#def game(int_board,turn):

def minimize(int_board,depth):
    cols=expand(int_board)
    board=extra_expand(cols)
    if depth == 0 or is_goal(board):
        return score(int_board) ,int_board
    neighbours=explore(int_board,1)
    best_move=1000000000
    best_neighbour=0
    for neighbour in neighbours:
        move=maximize(neighbour,depth-1)
        if move[0]< best_move:
            best_move=move[0]
            best_neighbour=neighbour
    return best_move, best_neighbour

def maximize(int_board,depth):
    cols = expand(int_board)
    board = extra_expand(cols)
    if depth == 0 or is_goal(board):
        return score(int_board) , int_board
    neighbours = explore(int_board, 1)
    best_move = -1000000000
    best_neighbour = 0
    for neighbour in neighbours:
        move = minimize(neighbour, depth - 1)
        if move[0] >best_move:
            best_move = move[0]
            best_neighbour = neighbour
    return best_move, best_neighbour


def minimize_beta(int_board,depth,alpha,beta):
    cols=expand(int_board)
    board=extra_expand(cols)
    if depth == 0 or is_goal(board):
        return score(int_board) ,int_board
    neighbours=explore(int_board,1)
    best_move=1000000000
    best_neighbour=0
    for neighbour in neighbours:
        move=maximize_alpha(neighbour,depth-1,alpha,beta)
        if move[0]< best_move:
            best_move=move[0]
            best_neighbour=neighbour
        if move[0] <= alpha:
            break
        if move[0] <beta:
            beta=move[0]

    return best_move, best_neighbour

def maximize_alpha(int_board,depth,alpha,beta):
    cols = expand(int_board)
    board = extra_expand(cols)
    if depth == 0 or is_goal(board):
        return score(int_board) , int_board
    neighbours = explore(int_board, 1)
    best_move = -1000000000
    best_neighbour = 0
    for neighbour in neighbours:
        move = minimize_beta(neighbour, depth - 1,alpha,beta)
        if move[0] >best_move:
            best_move = move[0]
            best_neighbour = neighbour
        if move[0] >= beta:
            break
        if move[0] > alpha:
            alpha=move[0]
    return best_move, best_neighbour

#def heuristic(int_board): #very weak heuristic

def explore(int_board,turn):#!!!!!!!PROBLEM IT OVERWRITES VALUES OF THE OTHER PLAYER MAYBE
    states=[]
    empty=[]
    cols=expand(int_board)
    board=extra_expand(cols)
    i=0
    if turn==1:
        i = 0
        for col in cols:
            first_empty = col[0:3]
            f_empty = int(first_empty, 2)
            tempboard = copy.deepcopy(board)
            # print(board)
            if f_empty != 0:
                tempboard[f_empty - 1][i] = 1
                states.append(extra_compress(tempboard))
            i = i + 1

    #elif turn==2:
    #     i = 0
    #         for col in cols:
    #             first_empty = col[0:3]
    #             f_empty = int(first_empty, 2)
    #             tempboard = copy.deepcopy(board)
    #             # print(board)
    #             if f_empty != 0:
    #                 tempboard[f_empty - 1][i] = 2
    #                 states.append(extra_compress(tempboard))
    #             i = i + 1
    return states

def score(int_board):
    cols=expand(int_board)
    board=extra_expand(cols)
    scoreai=0
    scorehi=0
    for i in range (6): #loops row by row
        for j in range(4):
            if board[i][j]==1 and board[i][j+1]==1 and  board[i][j+2]==1 and board[i][j+3]==1:
                scoreai=scoreai+1
            elif board[i][j]==2 and board[i][j+1]==2 and  board[i][j+2]==2 and board[i][j+3]==2:
                scorehi=scorehi+1

    for i in range(7):  # loops column by column
        for j in range(3):
            if board[j][i] == 1 and board[j+1][i] == 1 and board[j+2][i] == 1 and board[j+3][i] == 1:
                scoreai = scoreai + 1
            elif board[j][i] == 2 and board[j+1][i] == 2 and board[j+2][i] == 2 and board[j+3][i] == 2:
                scorehi = scorehi + 1

    for i in range (3):
        for j in range (4):
            if board[i][j] == 1 and board[i+1][j + 1] == 1 and board[i+2][j + 2] == 1 and board[i+3][j + 3] == 1:
                scoreai = scoreai + 1
            elif board[i][j] == 2 and board[i+1][j + 1] == 2 and board[i+2][j + 2] == 2 and board[i+3][j + 3] == 2:
                scorehi = scorehi + 1
    score_diff=scoreai-scorehi
    return score_diff


if __name__ == '__main__':
    board=[
        #0,1,2,3,4,5,6
        [0,0,0,0,0,0,0],#row 1
        [0,0,0,0,0,0,0],#row 2
        [0,0,0,0,0,0,0],#row 3
        [0,0,0,0,0,0,0],#row 4
        [2,1,2,1,2,1,2],#row 5
        [1,2,1,2,1,2,1] #row 6
    ]


    f=extra_compress(board)
    cols=expand(f)
    move=maximize_alpha(f,8,-2000,2000)
    newboard=move[1]
    newcols=expand(newboard)
    newf=extra_expand(newcols)
    for i in range (6):
        print(newf[i])