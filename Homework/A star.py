import heapq

grid_map = [
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0]
]

start = (0, 0)
end = (9, 9)

open_list = []
heapq.heappush(open_list, (0, start))

closed_list = []
parent = {}

while open_list:
    distance, current = heapq.heappop(open_list)

    if current in closed_list:
        continue

    if current == end:
        break

    closed_list.append(current)
    x, y = current

    def addNode(next_node):
        if (next_node not in closed_list) and (grid_map[next_node[0]][next_node[1]] != 1):
            next_distance = distance + 1 + abs(end[0] - next_node[0]) + abs(end[1] - next_node[1])
            heapq.heappush(open_list, (next_distance, next_node))
            parent[str(next_node)] = current

    if x - 1 >= 0:
        next_node = (x - 1, y)
        addNode(next_node)

    if y - 1 >= 0:
        next_node = (x, y - 1)
        addNode(next_node)

    if x + 1 < 10:
        next_node = (x + 1, y)
        addNode(next_node)

    if y + 1 < 10:
        next_node = (x, y + 1)
        addNode(next_node)

current = end
print(current)
while current != start:
    current = parent[str(current)]
    print(current)