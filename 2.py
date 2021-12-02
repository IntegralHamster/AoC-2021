import re

f = open('input.txt', 'r')
inp = []
for line in f:
    if line == '<>':
        break
    inp.append(line.strip())

# part 1
x = 0
y = 0
for i in range(len(inp)):
    command = re.split(' ', inp[i])
    if command[0][0] == 'f':
        x += int(command[1])
    elif command[0][0] == 'd':
        y += int(command[1])
    elif command[0][0] == 'u':
        y -= int(command[1])
print(x*y)

#part 2
x = 0
y = 0
aim = 0
for i in range(len(inp)):
    command = re.split(' ', inp[i])
    if command[0][0] == 'f':
        x += int(command[1])
        y += aim*int(command[1])
    elif command[0][0] == 'd':
        aim += int(command[1])
    elif command[0][0] == 'u':
        aim -= int(command[1])
print(x*y)