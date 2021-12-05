def add_line(grid,line):
    start = line[0]
    end = line[1]

    if start[0] == end[0]:
        x_inc = 0
    else:
        x_inc = int((end[0] - start[0]) / abs((end[0] - start[0]))) 
    if start[1] == end[1]:
        y_inc = 0
    else:
        y_inc = int((end[1] - start[1]) / abs((end[1] - start[1]))) 

    new_overlap = 0
    for i in range(max(abs(start[0] - end[0]), abs(start[1] - end[1])) + 1):
        if grid[start[0] + i*x_inc][start[1] + i*y_inc] == 1:
            new_overlap += 1
        grid[start[0] + i*x_inc][start[1] + i*y_inc] += 1
    
    return new_overlap


lines = []
with open ('input.txt','r') as f:
    for inp in f:
        line = []
        inp = inp.strip()
        start, stop = inp.split(' -> ')
        line.append(list(map(int, start.split(','))))
        line.append(list(map(int, stop.split(','))))
        lines.append(line)

grid = [[0]*1000 for i in range(1000)]
overlap = 0
for line in lines:
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        overlap += add_line(grid,line)
print(overlap) #part 1 answer

grid = [[0]*1000 for i in range(1000)]
overlap = 0
for line in lines:
    overlap += add_line(grid,line)
print(overlap) #part 2 answer