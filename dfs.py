import networkx as nx
from matplotlib import pyplot as plt

def dfs(G, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in G[node]:
            dfs(G, neighbor, visited)

G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
visited = []
dfs(G, 'A', visited)
print(visited)

    