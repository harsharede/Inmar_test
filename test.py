import sys, argparse

column = ['a','b','c','d','e','f','g','h']
row = [8,7,6,5,4,3,2,1]
moves = ['move_down','move_up','move_right','move_left']
directions_flag = {'move_down':1,'move_up':1,'move_right':2,'move_left':2}
xy = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

board =[]

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


# building chess board
for current_row in row:
    line = []
    for current_column in column:
        value = current_column+str(current_row)
        line.append(value)

    board.append(line)

for i in board:
    print(i)

def getposition(position):

    return [position[0], int(position[-1])]


def Knight(position):
    print position
    possible_moves = []
    moves = ['move_down', 'move_up', 'move_right', 'move_left']
    for i in moves:
        for j in moves:
            now = getposition(position)
            # print i,j
            if i != j:
                if directions_flag[i] != directions_flag[j]:
                    print "result:", i, j, j
                    # print now
                    if getattr(sys.modules[__name__], i)(now) != None:
                        now = getattr(sys.modules[__name__], i)(now)
                        print i, now
                        if getattr(sys.modules[__name__], j)(now) != None:
                            now = getattr(sys.modules[__name__], j)(now)
                            print j, now
                            if getattr(sys.modules[__name__], j)(now) != None:
                                now = getattr(sys.modules[__name__], j)(now)
                                print j, now
                                possible_moves.append(now)


    return possible_moves

print Knight('a7')