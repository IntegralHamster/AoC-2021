def card_sum(card):
    sum = 0
    for i in card:
        for j in i:
            if j != -1:
                sum += j
    return sum

def bingo(balls,cards):
    for i in balls:
        for j in cards:
            for k in range(5):
                for l in range(5):
                    if j[k][l] == i:
                        j[k][l] = -1
            for k in range(5):
                if j[k] == [-1,-1,-1,-1,-1] or (j[0][k] == j[1][k] == j[2][k] == j[3][k] == j[4][k] == -1):
                    return i*card_sum(j)

def bingo2(balls,cards):
    flag = []
    last = []
    last_ball = -1
    for i in balls:
        for j in cards:
            if j not in flag:
                for k in range(5):
                    for l in range(5):
                        if j[k][l] == i:
                            j[k][l] = -1
                for k in range(5):
                    if j[k] == [-1,-1,-1,-1,-1] or (j[0][k] == j[1][k] == j[2][k] == j[3][k] == j[4][k] == -1):
                        last = j
                        last_ball = i
                        flag.append(j)
    return last_ball*card_sum(last)

f = open('input.txt', 'r')

cards = []
flag = 0
for line in f:
    if ',' in line:
        balls = [int(x) for x in line.split(',')]
    elif line == '\n':
        if flag == 1:
            cards.append(card)
        card = []
        flag = 1
    else:
        card.append([int(x) for x in line.split()])

cards.append(card)
print(bingo(balls,cards)) #part 1 answer
print(bingo2(balls,cards)) #part 2 answer




