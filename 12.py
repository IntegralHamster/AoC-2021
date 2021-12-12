nodes = []
vertices = []
with open ('input.txt','r') as f:
    for line in f:
        line = line.strip()
        left, right = line.split('-')
        vertices.append([left,right])
        if left not in nodes:
            nodes.append(left)
        if right not in nodes:
            nodes.append(right)

adj_list = {}

for vertice in vertices:
    tmp = []
    if vertice[0] not in adj_list:
        tmp.append(vertice[1])
        adj_list[vertice[0]] = tmp
    else:
        tmp.extend(adj_list[vertice[0]])
        tmp.append(vertice[1])
        adj_list[vertice[0]] = tmp
    tmp = []
    if vertice[1] not in adj_list:
        tmp.append(vertice[0])
        adj_list[vertice[1]] = tmp
    else:
        tmp.extend(adj_list[vertice[1]])
        tmp.append(vertice[0])
        adj_list[vertice[1]] = tmp   

def way(adj_list, visited, node):
    if node == 'start':
        return 1
    else:
        visited.append(node)
        ways = 0
        for choice in adj_list[node]:
            if not((choice.islower()) and (choice in visited)):               
                visit = visited.copy()
                ways += way(adj_list, visit, choice)
        return ways

visited = []
print(way(adj_list, visited, 'end')) #part 1 answer

def way2(adj_list, visited, node):
    if node == 'start':
        return 1
    else:
        visited.append(node)
        ways = 0
        double_visit_flag = False
        for vis in visited:
            if vis.islower() and visited.count(vis) > 1:
                double_visit_flag = True
        for choice in adj_list[node]:
            if choice != 'end' and not((choice.islower()) and (choice in visited) and (double_visit_flag == True)):                               
                visit = visited.copy()
                ways += way2(adj_list, visit, choice)
        return ways

visited = []
print(way2(adj_list, visited, 'end')) #part 1 answer