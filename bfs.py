import networkx as nx
from matplotlib import pyplot as plt

def bfs(G, start):
    vistied, queue = [], [start]
    while queue:
        vistied.append(queue[0])
        for node in list(G.neighbors(queue[0])):
            if node not in vistied and node not in queue:
                queue.append(node)
        queue.pop(0)
    return vistied

G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
visited = bfs(G, 'A')
print(visited)
nx.draw_networkx(G)
plt.show()