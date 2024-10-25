import networkx as nx
from matplotlib import pyplot as plt
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)  # 将节点添加到已访问列表中
        
        # 遍历当前节点的邻居
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)  # 递归调用，不需要返回值

# 示例图
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 初始化已访问节点的列表
visited = []

# 从节点 'A' 开始进行 DFS
dfs(graph, 'A', visited)

# 打印访问顺序
print(visited)
