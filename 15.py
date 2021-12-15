from queue import PriorityQueue

danger = []
with open ('input.txt','r') as f:
    for line in f:
        danger.append(line.strip())

edge_list = []
for i in range(len(danger)):
    for j in range(len(danger[i])):
        if j + 1 < len(danger[i]):
            edge_list.append([i*len(danger[i]) + j, i*len(danger[i]) + j + 1, int(danger[i][j]) + int(danger[i][j+1])])
        if i + 1 < len(danger):
            edge_list.append([i*len(danger[i]) + j, (i+1)*len(danger[i]) + j, int(danger[i+1][j]) + int(danger[i][j])])

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = {}
        self.neighbors = {}
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[(u,v)] = weight
        self.edges[(v,u)] = weight
        tmp = []
        if u not in self.neighbors:
            tmp.append(v)
            self.neighbors[u] = tmp
        else:
            tmp.extend(self.neighbors[u])
            tmp.append(v)
            self.neighbors[u] = tmp
        tmp = []
        if v not in self.neighbors:
            tmp.append(u)
            self.neighbors[v] = tmp
        else:
            tmp.extend(self.neighbors[v])
            tmp.append(u)
            self.neighbors[v] = tmp   


g = Graph(len(danger)*len(danger[0]))
for edge in edge_list:
    g.add_edge(edge[0],edge[1],edge[2])

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        if current_vertex % 1000 == 0:
            print(current_vertex)
        for neighbor in graph.neighbors[current_vertex]:
            distance = graph.edges[(current_vertex, neighbor)]
            if neighbor not in graph.visited:
                old_cost = D[neighbor]
                new_cost = D[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost
    return D

D = dijkstra(g,0)

print((D[len(danger)*len(danger[0]) - 1] - int(danger[0][0]) + int(danger[len(danger)-1][len(danger[0])-1])) / 2) #part 1 answer

big_danger = [[0]*5*len(danger[0]) for i in range(5*len(danger))]

for i in range(len(big_danger)):
    for j in range(len(big_danger[i])):
        big_danger[i][j] = (int(danger[i % len(danger)][j % len(danger[0])]) + (i // len(danger)) + (j // len(danger)))
        if big_danger[i][j] > 9:
            big_danger[i][j] = big_danger[i][j] % 9


big_edge_list = []
for i in range(len(big_danger)):
    for j in range(len(big_danger[i])):
        if j + 1 < len(big_danger[i]):
            big_edge_list.append([i*len(big_danger[i]) + j, i*len(big_danger[i]) + j + 1, big_danger[i][j] + big_danger[i][j+1]])
        if i + 1 < len(big_danger):
            big_edge_list.append([i*len(big_danger[i]) + j, (i+1)*len(big_danger[i]) + j, big_danger[i+1][j] + big_danger[i][j]])

g2 = Graph(len(big_danger)*len(big_danger[0]))
for edge in big_edge_list:
    g2.add_edge(edge[0],edge[1],edge[2])

D = dijkstra(g2,0)

print((D[len(big_danger)*len(big_danger[0]) - 1] - int(big_danger[0][0]) + int(big_danger[len(big_danger)-1][len(big_danger[0])-1])) / 2) #part 2 answer