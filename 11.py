octo = []
with open ('input.txt','r') as f:
    for line in f:
        octo.append(line.strip())

octo_walls = [[10] * (len(octo[0])+2) for i in range(len(octo) + 2)]

for i in range(len(octo)):
    for j in range(len(octo[i])):
        octo_walls[i+1][j+1] = int(octo[i][j])

def flash_step(octo_walls, octo):
    flash_coord = []
    for i in range(len(octo)):
        for j in range(len(octo[i])):
            octo_walls[i+1][j+1] += 1
    no_flashes = 1
    while no_flashes == 1:
        no_flashes = 0
        for i in range(len(octo)):
            for j in range(len(octo[i])):
                if octo_walls[i+1][j+1] > 9 and ([i,j] not in flash_coord):
                    flash_coord.append([i,j])
                    no_flashes = 1
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if (dx != 0) or (dy != 0):
                                octo_walls[i+1+dx][j+1+dy] += 1
    for flash_point in flash_coord:
        octo_walls[flash_point[0] + 1][flash_point[1] + 1] = 0
    return len(flash_coord)

flashes = 0
step = 0
while True:
    step += 1
    inc_flashes = flash_step(octo_walls, octo)
    flashes += inc_flashes
    if step == 100:
        print(flashes) #part 1 answer
    if inc_flashes == len(octo)*len(octo[0]):
        print(step) #part 2 answer
        break




