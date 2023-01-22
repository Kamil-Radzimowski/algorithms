graph_1 = {
    'Amin': {'Wasim', 'Nick', 'Mike'},
    'Wasim': {'Imran', 'Amin'},
    'Imran': {'Wasim', 'Faras'},
    'Faras': {'Imran'},
    'Mike': {'Amin'},
    'Nick': {'Amin'}
}


def bfs(graph, start, lookFor):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop()
        if node == lookFor:
            return node
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return None


print(bfs(graph_1, 'Amin', 'Faras'))
print(bfs(graph_1, 'Amin', 'Kamil'))


