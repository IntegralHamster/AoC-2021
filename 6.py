with open ('input.txt','r') as f:
    for line in f:
        fish = [int(x) for x in (line.strip()).split(',')]

for day in range(80):
    for j in range(len(fish)):
        fish[j] -= 1
        if fish[j] == -1:
            fish.append(8)
            fish[j] = 6

print(len(fish)) # part 1 answer, don't judge me

for day in range(48):
    for j in range(len(fish)):
        fish[j] -= 1
        if fish[j] == -1:
            fish.append(8)
            fish[j] = 6

fish_count = [0] * 9
for i in range(len(fish)):
    fish_count[fish[i]] += 1

fish_test = []
for i in range(9):
    fish_test.append([i,i])

for day in range(128):
    for j in range(len(fish_test)):
        fish_test[j][0] -= 1
        if fish_test[j][0] == -1:
            fish_test.append([8,fish_test[j][1]])
            fish_test[j][0] = 6

fish_test_count = [0]*9
for i in range(len(fish_test)):
    fish_test_count[fish_test[i][1]] += 1

print(sum([x*y for x,y in(zip(fish_count,fish_test_count))])) #part 2 answer, still don't judge me