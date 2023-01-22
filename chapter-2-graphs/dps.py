graph_1 = {
    'Amin': {'Wasim', 'Nick', 'Mike'},
    'Wasim': {'Imran', 'Amin'},
    'Imran': {'Wasim', 'Faras'},
    'Faras': {'Imran'},
    'Mike': {'Amin'},
    'Nick': {'Amin'}
}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


dfs(graph_1, 'Amin')
