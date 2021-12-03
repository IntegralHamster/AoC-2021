inp = []
with open ('input.txt','r') as f:
    for line in f:
        inp.append(line.strip())

ans = [[0]*2  for i in range(len(inp[0]))] 

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == '0':
            ans[j][0] += 1
        else:
            ans[j][1] += 1

most = 0
least = 0
ord = 0
for i in range(len(ans)):
    if int(ans[len(ans)-i-1][0]) > int(ans[len(ans)-i-1][1]):
        digit = 0
    else:
        digit = 1
    most += digit*(2**ord)
    least += (1 - digit)*(2**ord)
    ord += 1

print(most*least) #part 1 answer


def digit_check (arr, pos, minmaxflag):
    num0 = 0
    num1 = 0
    for i in range(len(arr)):
        if int(arr[i][pos]) == 0:
            num0 += 1
        else:
            num1 += 1
    if minmaxflag == 1:
        if num1 >= num0:
            correct = 1
        else:
            correct = 0
    else:
        if num1 < num0:
            correct = 1
        else:
            correct = 0
    out = []
    for i in range(len(arr)):
        if int(arr[i][pos]) == correct:
            out.append(arr[i])

    return out

inp2 = inp[:]
pos = 0
while len(inp2) > 1:
    inp2 = digit_check(inp2, pos, 1)[:]
    pos += 1
most2 = inp2[0]

inp2 = inp[:]
pos = 0
while len(inp2) > 1:
    inp2 = digit_check(inp2, pos, 0)[:]
    pos += 1
least2 = inp2[0]

most = 0
least = 0
ord = 0
for i in range(len(most2)):
    most += int(most2[len(most2) - i - 1]) * (2 ** ord)
    least += int(least2[len(least2) - i - 1]) * (2 ** ord)
    ord += 1
    
print(most*least) #part 2 answer