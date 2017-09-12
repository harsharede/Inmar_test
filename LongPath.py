import sys, argparse

column = ['a','b','c','d','e','f','g','h']
row = [8,7,6,5,4,3,2,1]
directions_flag = {'move_down':1,'move_up':1,'move_right':2,'move_left':2}
board =[]

# building chess board
for current_row in row:
    line = []
    for current_column in column:
        value = current_column+str(current_row)
        line.append(value)

    board.append(line)

# Printing Chess board for reference
for i in board:
    print(i)

# Below fucntion help in moving piece position by 1 in respective directions
def move_down(now):
    if int(now[1]) != 1:
        return board[(8 - int(now[1])) + 1][column.index(now[0])]

def move_down_right(now):
    if int(now[1]) != 1 and now[0] != "h":
        return board[(8 - int(now[1])) + 1][column.index(now[0])+1]

def move_down_left(now):
    if int(now[1]) != 1 and now[0] != "a":
        return board[(8 - int(now[1])) + 1][column.index(now[0])-1]

def move_up(now):
    if int(now[1]) < 8:
        return board[(8 - int(now[1])) - 1][column.index(now[0])]

def move_up_right(now):
    if int(now[1]) < 8 and now[0] != "h":
        return board[(8 - int(now[1])) - 1][column.index(now[0])+1]

def move_up_left(now):
    if int(now[1]) < 8 and now[0] != "a":
        return board[(8 - int(now[1])) - 1][column.index(now[0])-1]

def move_right(now):
    if now[0] != "h":
        return board[(8 - int(now[1]))][column.index(now[0]) + 1]

def move_left(now):
    if now[0] != "a":
        return board[(8 - int(now[1]))][column.index(now[0]) - 1]


# Return postion as list
def getposition(position):
    return [position[0], int(position[-1])]


# Returns path of a piece when postion and direction is provided
def inpath(position, direction):
    now = getposition(position)
    path = []
    for i in range(1,9):
        if getattr(sys.modules[__name__], direction)(now) == None:
            break
        now = getattr(sys.modules[__name__], direction)(now)
        path.append(now)
        now = getposition(now)
    return path

# Finds longest length and check if current tile comes under target
def path_len_tile(path, target):
    # print target
    if path:
        result = None
        for i in path:
            # print i
            if i in target:
                # print "In target"
                result = i, path.index(i)
                break
        # print result
        if result == None:
            result = path[-1], path.index(path[-1])
    else:
        result = 0,0
    # print result
    return result

# Function to find longest path for Queen
def QUEEN_long_path(position, target):
    now = getposition(position)
    moves = ['move_down', 'move_up', 'move_right', 'move_left', 'move_down_right', 'move_down_left', 'move_up_right',
             'move_up_left']
    steps = 0
    long_position = ''
    for i in moves:
        # print i
        path = inpath(position, i)
        # print path
        long_tile = path_len_tile(path, target)
        # print long_tile
        if long_tile[1] > steps:
            steps = long_tile[1]
            long_position = long_tile[0]

    return [long_position, steps+1]


# Function to find longest path for Rook
def ROOK_long_path(position, target):
    now = getposition(position)
    moves = ['move_down', 'move_up', 'move_right', 'move_left']

    steps = 0
    long_position = ''
    for i in moves:
        path = inpath(position, i)
        # print path
        long_tile = path_len_tile(path, target)
        # print long_tile
        if long_tile[1] > steps:
            steps = long_tile[1]
            long_position = long_tile[0]

    return [long_position, steps + 1]

# print ROOK_long_path('h5')

# Function to find longest path for Knigh
def Knight_long_path(position, target):
    possible_moves = []
    moves = ['move_down', 'move_up', 'move_right', 'move_left']
    for i in moves:
        for j in moves:
            now = getposition(position)
            # print i,j
            if i != j:
                if directions_flag[i] != directions_flag[j]:
                    # print "result:", i, j, j
                    # print now
                    if getattr(sys.modules[__name__], i)(now) != None:
                        now = getattr(sys.modules[__name__], i)(now)
                        # print i, now
                        if getattr(sys.modules[__name__], j)(now) != None:
                            now = getattr(sys.modules[__name__], j)(now)
                            # print j, now
                            if getattr(sys.modules[__name__], j)(now) != None:
                                now = getattr(sys.modules[__name__], j)(now)
                                # print j, now
                                possible_moves.append((now,3))

    return possible_moves

# print Knight_long_path('d2')

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

    print target

    if piece == 'KNIGHT':
        print Knight_long_path(position, target)
    elif piece == 'QUEEN':
        print QUEEN_long_path(position, target)
    elif piece == 'ROOK':
        print ROOK_long_path(position, target)
    else:
        print "piece not found"



if __name__=="__main__":
    main()
