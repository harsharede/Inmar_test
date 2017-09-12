import sys, argparse

column = ['a','b','c','d','e','f','g','h']
row = [8,7,6,5,4,3,2,1]
moves = ['move_down','move_up','move_right','move_left']
directions_flag = {'move_down':1,'move_up':1,'move_right':2,'move_left':2}
xy = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

board =[]


def move_down(now,m):
    return board[(8 - int(now[1])) + m][column.index(now[0])]

def move_up(now,m):
    if ((8 - int(now[1])) - 1)>0:
        return board[(8 - int(now[1])) - m][column.index(now[0])]

def move_right(now,m):
    return board[(8 - int(now[1]))][column.index(now[0]) + m]

def move_left(now,m):
    if (column.index(now[0]) - 1) > 0:
        return board[(8 - int(now[1]))][column.index(now[0]) - m]






def current_position(now):
    return board[(8-int(now[1]))][column.index(now[0])]

for current_row in row:
    line = []
    for current_column in column:
        value = current_column+str(current_row)
        line.append(value)

    board.append(line)

for i in board:
    print(i)

def getposition(position):
    column_position = position[0]
    row_postion = int(position[-1])
    return [column_position, row_postion]


def Knight(position):
    possible_moves = []
    # print current_position(getposition(position))
    for i in range(len(moves)):
        for j in moves:
            now = position
            if moves[i] != j:
                if directions_flag[moves[i]] != directions_flag[j]:
                    try:
                        now = getattr(sys.modules[__name__], moves[i])(now,1)
                        # print now
                        now = getattr(sys.modules[__name__], j)(now,2)
                        # print now
                        if now != None:
                            possible_moves.append(now)
                    except:
                        pass
    return possible_moves

def conevert_2_xy(now):
    return [xy[now[0]],now[1]]

def xy_2_position(now):
    return str(column[now[0]])+str(now[1])

def ROOK(position):

    now = getposition(position)
    possible_moves = [str(x) + str(now[1]) for x in column]
    possible_moves.pop(possible_moves.index(position))
    possible_moves += [str(now[0]) + str(x) for x in row]
    possible_moves.pop(possible_moves.index(position))
    return possible_moves


def QUEEN(position, set):
    now = getposition(position)
    possible_moves = []
    if set == "a" or set == 'all':
        possible_moves = [str(x) + str(now[1]) for x in column]
        possible_moves.pop(possible_moves.index(position))
    if set == "a":
        return possible_moves

    if set == "b" or set == 'all':
        possible_moves += [str(now[0]) + str(x) for x in row]
        possible_moves.pop(possible_moves.index(position))
    if set == "b":
        return possible_moves[::-1]

    k = int(column.index(now[0]))
    if set == "c" or set == 'all':
        count = 0
        for i in range(1, 9):
            # print i
            if i < now[1] and k + i < 8:
                possible_moves.insert(0,column[k + i] + str(now[1] - i))
            elif i > now[1]:
                if count >= len(column[:k][::-1]):
                    # print "break"
                    break
                possible_moves.append(column[:k][::-1][count] + str(now[1] + count + 1))
                count += 1
    if set == "c":
        return possible_moves[::-1]

    if set == "d" or set == 'all':
        count = 0
        for i in range(1, 9):
            # print i, column[k - i], k-i
            if i < now[1] and k - i >= 0:
                possible_moves.insert(0,column[k - i] + str(now[1] - i))
                # break
            elif i > now[1]:
                if count + 1 >= len(column[k:]):
                    # print "break"
                    break
                possible_moves.append(column[k:][count + 1] + str(now[1] + count + 1))
                count += 1
    if set == "d":
        return possible_moves
    if set == "all":
        return possible_moves

def find_long_path(position,path):


    print position, path
    now = getposition(position)
    print now[0], now[1]
    if getposition(path[0])[0] != getposition(path[1])[0]:
        print

def get_target(piece,position,target ):

    if piece == 'QUEEN':
        a = QUEEN(position, 'a')
        b = QUEEN(position, 'b')
        c = QUEEN(position, 'c')
        d = QUEEN(position, 'd')

        print "##################################################################"
        print a
        print b
        print c
        print d

        print len(a),len(b), len(c), len(d)
        print find_long_path(position,a )


    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-piece","--piece", help='pass your piece', choices=['QUEEN','ROOK','KNIGHT'])
    parser.add_argument("-position", "--position", help='pass current position of piece')

    parser.add_argument("-target", "--target",nargs='+', help='''Please select 8 pieces positions on below chess board.

['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6']
['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5']
['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4']
['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3']
['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']

    ''')

    args = parser.parse_args()

    piece = str(args.piece)
    position = str(args.position)
    target = args.target

    # print target
    # for i in target:
    #     print i

    target = ['a1','e5','g5','h8','b6','f3','d3','h3']

    if piece == 'KNIGHT':
        print Knight(position)
    elif piece == 'QUEEN':
        print QUEEN(position,set='a')
    elif piece == 'ROOK':
        print ROOK(position)
    else:
        print "piece not found"



if __name__=="__main__":
    # print QUEEN("d2",'a')

    get_target(piece = 'QUEEN', position="d2", target=['a1','e5','g5','h8','b6','f3','d3','h3'])
    position = 'g2'
    # print QUEEN(position, set='c')
    # print '######################################################################'
    # print QUEEN(position, set='c')
    # print QUEEN(position, set='d')
    # print QUEEN(position, set='a')
    # print QUEEN(position, set='b')
    # print QUEEN(position, set='a')
    # print QUEEN(position, set='b')





    # main()
    # print "done"
