import networkx as nx
from matplotlib import pyplot as plt
# 有向图和无向图
# G = nx.Graph() 
G = nx.DiGraph()
G.add_edges_from([('1', '2'), ('1', '3'), ('2', '4'), ('2', '5'), ('3', '6'), ('3', '7')])
nx.draw_networkx(G)
plt.show()

WG = nx.DiGraph()
WG.add_edges_from([('A', 'B', {"weight": 10}), ('A', 'C', {"weight": 20}), 
                   ('B', 'D', {"weight": 30}), ('B', 'E', {"weight": 40}), 
                   ('C', 'F', {"weight": 50}), ('C', 'G', {"weight": 60})])
labels = nx.get_edge_attributes(WG, 'weight')
pos=nx.spring_layout(WG)
nx.draw_networkx(WG, pos)
nx.draw_networkx_edge_labels(WG, pos, edge_labels=labels)
plt.show()

# 连通图和非连通图
g1 = nx.Graph()
g1.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 5)])
print(f"Is graph 1 connected? {nx.is_connected(g1)}")
g2 = nx.Graph()
g2.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4)])
print(f"Is graph 2 connected? {nx.is_connected(g2)}")
plt.subplot(121)
nx.draw_networkx(g1, pos=nx.spring_layout(g1))
plt.subplot(122)
nx.draw_networkx(g2, pos=nx.spring_layout(g2))
plt.show()

# 节点的度
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
print(f"deg(A) = {G.degree['A']}")
DG = nx.DiGraph()
DG.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
print(f"deg^-(A) = {DG.in_degree['A']}")
print(f"deg^+(A) = {DG.out_degree['A']}")

# 中心性
print(f"Degree centrality      = {nx.degree_centrality(G)}")
print(f"Closeness centrality   = {nx.closeness_centrality(G)}")
print(f"Betweenness centrality = {nx.betweenness_centrality(G)}")

#广度优先搜索
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
vistied, queue = set(), [G.nodes[0]]
while queue:
    print(queue[0])
    vistied.add(queue[0])
    for node in G.neighbors(queue[0]):
        if node not in vistied:
            queue.append(node)
    vistied.remove(queue[0])


