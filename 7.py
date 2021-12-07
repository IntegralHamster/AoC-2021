with open ('input.txt','r') as f:
    for line in f:
        crabs = [int(x) for x in (line.strip()).split(',')]

dist1 = []
dist2 = []
for i in range(max(crabs)):
    tot1 = 0
    tot2 = 0
    for j in range(len(crabs)):
        tot1 += abs(i - crabs[j])
        tot2 += int((abs(i - crabs[j]))*(abs(i - crabs[j]) + 1) / 2)
    dist1.append(tot1)
    dist2.append(tot2)

print(min(dist1)) #part 1 answer
print(min(dist2)) #part 2 answer
