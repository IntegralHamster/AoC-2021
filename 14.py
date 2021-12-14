poly_dict = {}
with open ('input.txt','r') as f:
    for line in f:
        if line == '\n':
            continue
        elif '->' in line:
            line = line.strip()
            left, right = line.split(' -> ')
            poly_dict[left] = right
        else:
            inp_str = line.strip()

start_poly = {}
for i in range(len(inp_str)-1):
    if inp_str[i:i+2] in start_poly.keys():
        start_poly[inp_str[i:i+2]] += 1
    else:
        start_poly[inp_str[i:i+2]] = 1

def polymerizing(start_poly, poly_dict):
    new_poly = {}
    for word in start_poly.keys():
        new_word1 = word[0] + poly_dict[word]
        new_word2 = poly_dict[word] + word[1]
        for i in [new_word1, new_word2]:
            if i in new_poly.keys():
                new_poly[i] += start_poly[word]
            else:
                new_poly[i] = start_poly[word]
    return new_poly

for i in range(40): #10 for part 1 answer, 40 for part 2
    start_poly = polymerizing(start_poly, poly_dict).copy()

def letter_count(start_poly, inp_str):
    count = {}
    for word in start_poly.keys():
        for letter in [word[0],word[1]]:
            if letter in count.keys():
                count[letter] += start_poly[word]
            else:
                count[letter] = start_poly[word]
    if inp_str[0] in count.keys():
        count[inp_str[0]] += 1
    else:
        count[inp_str[0]] = 1
    if inp_str[-1] in count.keys():
        count[inp_str[-1]] += 1
    else:
        count[inp_str[-1]] = 1
    return count

count = letter_count(start_poly, inp_str)

sorted_keys = sorted(count, key = count.get)
print((count[sorted_keys[-1]] - count[sorted_keys[0]]) // 2)    
