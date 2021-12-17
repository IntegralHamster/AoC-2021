x_1 = 230
x_2 = 283
y_1 = -57
y_2 = -107

x_1 = 185
x_2 = 221
y_1 = -74
y_2 = -122

x_speed = {}
for v in range(1,x_2 + 1):
    x = 0
    time = 0
    time_low = -1
    time_high = -1
    stall_flag = False
    v_x = v
    while x <= x_2:
        x += v_x
        time += 1
        v_x -= 1
        if x >= x_1 and x <= x_2 and time_low == -1:
            time_low = time
        if v_x == 0:
            stall_flag = True
            break
    if stall_flag == True:
        time_high = 99999
    else:
        time_high = time - 1
    if time_low != -1:
        x_speed[v] = [time_low, time_high]

y_speed = {}
for v in range(y_2 - 1, -y_2 + 1):
    y = 0
    time = 0
    time_low = -1
    time_high = -1
    v_y = v
    while y >= y_2:
        y += v_y
        time += 1
        v_y -= 1
        if y <= y_1 and y >= y_2 and time_low == -1:
            time_low = time
    time_high = time - 1
    if time_low != -1:
        y_speed[v] = [time_low, time_high] 

possible_speeds = []
for x_s in x_speed.keys():
    for y_s in y_speed.keys():
        if (x_speed[x_s][0] <= y_speed[y_s][0] <= x_speed[x_s][1]) or (x_speed[x_s][0] <= y_speed[y_s][1] <= x_speed[x_s][1]) or (y_speed[y_s][0] <= x_speed[x_s][0] <= y_speed[y_s][1]) or (y_speed[y_s][0] <= x_speed[x_s][1] <= y_speed[y_s][1]) :
            possible_speeds.append([x_s, y_s])

print(len(possible_speeds))
