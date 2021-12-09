lava = []
with open ('input.txt','r') as f:
    for line in f:
        lava.append(line.strip())

lava_walls = [[10] * (len(lava[0])+2) for i in range(len(lava) + 2)]

for i in range(len(lava)):
    for j in range(len(lava[i])):
        lava_walls[i+1][j+1] = int(lava[i][j])


low_points_total = 0
low_points = []
for i in range(len(lava)):
    for j in range(len(lava[i])):
        if (lava_walls[i+1][j+1] < lava_walls[i][j+1]) and (lava_walls[i+1][j+1] < lava_walls[i+2][j+1]) and (lava_walls[i+1][j+1] < lava_walls[i+1][j]) and (lava_walls[i+1][j+1] < lava_walls[i+1][j+2]):
            low_points_total += lava_walls[i+1][j+1] + 1
            low_points.append([i+1,j+1])

print(low_points_total) #part 1 answer

basin_size = [0 for i in range(len(low_points))]

def basin(lava_walls, low_points, i, j):
    if lava_walls[i+1][j+1] >= 9:
        return -1
    elif [i+1,j+1] in low_points:
        return low_points.index([i+1,j+1])
    else:
        if lava_walls[i+1][j+1] > lava_walls[i][j+1]:
            return basin(lava_walls, low_points, i-1, j)
        elif lava_walls[i+1][j+1] > lava_walls[i+2][j+1]:
            return basin(lava_walls, low_points, i+1, j)
        elif lava_walls[i+1][j+1] > lava_walls[i+1][j]:
            return basin(lava_walls, low_points, i, j-1)
        elif lava_walls[i+1][j+1] > lava_walls[i+1][j+2]:
            return basin(lava_walls, low_points, i, j+1)       

for i in range(len(lava)):
    for j in range(len(lava[i])):
        num = basin(lava_walls,low_points,i,j)
        if num != -1:
            basin_size[num] += 1

basin_sort = sorted(basin_size)
print(basin_sort[-1]*basin_sort[-2]*basin_sort[-3])