inp_dig = []
inp_num = []
with open ('input.txt','r') as f:
    for line in f:
        line = line.strip()
        left, right = line.split(' | ')
        digits = left.split(' ')
        number = right.split(' ')
        inp_dig.append(digits)
        inp_num.append(number)

easy_number_count = 0
easy_numbers = {2, 3, 4, 7}
for test in inp_num:
    for num in test:
        if len(num) in easy_numbers:
            easy_number_count += 1

print(easy_number_count) #part 1 answer

def string_dif(str1, str2):
    dif = ''
    for ch in str1:
        if ch not in str2:
            dif += ch
    return dif


def digit_deduction(inp):
    digits = sorted(inp, key = len)
    decoded = {'1': digits[0], '7': digits[1], '4': digits[2], '8': digits[9]}
    dig5 = [digits[3], digits[4], digits[5]]
    dig6 = [digits[6], digits[7], digits[8]]

    for di in dig6:
        if string_dif(decoded['1'], di) == '' and string_dif(decoded['7'], di) == '' and string_dif(decoded['4'], di) == '':
            decoded['9'] = di
            dig6.remove(di)

    left_low = string_dif(decoded['8'],decoded['9'])

    for di in dig5:
        if string_dif(decoded['7'], di) == '':
            decoded['3'] = di
        elif left_low in di:
            decoded['2'] = di
        else:
            decoded['5'] = di

    for di in dig6:
        if string_dif(decoded['5'], di) == '':
            decoded['6'] = di
        else:
            decoded['0'] = di

    inv_decoded = {v: k for k, v in decoded.items()}    

    return inv_decoded

ans = 0
for i in range(len(inp_dig)):
    decoded = digit_deduction(inp_dig[i])
    num_decoded = ''
    for num in inp_num[i]:
        for key in decoded.keys():
            if string_dif(num,key) == string_dif(key,num) == '':
                num_decoded += decoded[key]
    ans += int(num_decoded)

print(ans)
