chunks = []
with open ('input.txt','r') as f:
    for line in f:
        chunks.append(line.strip())

proper_chunks = dict([('(',')'), ('<','>'), ('[',']'), ('{','}')])
errors = dict([(')',3),(']',57),('}', 1197), ('>', 25137)])
fixing = dict([(')',1),(']',2),('}', 3), ('>', 4)])

error_sum = 0
fixing_score = []
for chunk in chunks:
    last_open = []
    break_flag = 0
    for char in chunk:
        if char in ['(', '<', '[', '{']:
            last_open.append(char)
        else:
            if proper_chunks[last_open[-1]] == char:
                last_open.pop()
            else:
                error_sum += errors[char]
                break_flag = 1
                break
    if break_flag == 0:
        score = 0
        for char in reversed(last_open):
            score *= 5
            score += fixing[proper_chunks[char]]
        fixing_score.append(score)
    

print(error_sum) #part 1 answer
print(sorted(fixing_score)[len(fixing_score) // 2]) #part 2 answer


