import matplotlib.pyplot as plt

dots = []
folds = []

with open ('input.txt','r') as f:
    for line in f:
        line = line.strip()
        if ',' in line:
            left, right = line.split(',')
            dots.append([int(left), int(right)])
        elif 'fold' in line:
            line = line.replace('fold along ','')
            left, right = line.split('=')
            folds.append([left, int(right)])

for fold in folds:
    if fold[0] == 'x':
        for dot in dots:
            if dot[0] > fold[1]:
                dot[0] = dot[0] - 2*(dot[0] - fold[1])
    elif fold[0] == 'y':
        for dot in dots:
            if dot[1] > fold[1]:
                dot[1] = dot[1] - 2*(dot[1] - fold[1])
    dots_new = []
    for dot in dots:
        if dot not in dots_new:
            dots_new.append(dot)
    dots = dots_new[:]
    if fold == folds[0]:
        print(len(dots))    #part 1 answer

x = []
y = []
for dot in dots:
    x.append(dot[0])
    y.append(dot[1])

plt.scatter(dots[:][0],dots[:][1])
plt.show() #part 2 answer after flipping and rotating a bit