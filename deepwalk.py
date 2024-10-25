import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
from gensim.models.word2vec import Word2Vec


G = nx.karate_club_graph()

labels = []
for node in G.nodes:
    label = G.nodes[node]['club']
    labels.append(1 if label == 'Officer' else 0)

plt.axis('off')
nx.draw_networkx(G, pos=nx.spring_layout(G, seed=0), node_color=labels)
plt.show()

def random_walk(start, length):
    walk = [str(start)]  # starting node
    
    for i in range(length):
        neighbors = [node for node in G.neighbors(start)]
        next_node = np.random.choice(neighbors, 1)[0]
        walk.append(str(next_node))
        start = next_node
    
    return walk

walks = []
for node in G.nodes:
    for _ in range(80):
        walks.append(random_walk(node, 10))

print(walks[0])
# ['0', '1', '30', '1', '3', '12', '3', '7', '3', '0', '17']

model = Word2Vec(walks,
                 hs=1,   # Hierarchical softmax
                 sg=1,   # Skip-gram
                 vector_size=100,
                 window=10,
                 workers=1)

print(f'Shape of W_embed: {model.wv.vectors.shape}')
# Shape of W_embed: (33, 10)

# Build vocabulary
model.build_vocab(walks)
# Train model
model.train(walks, total_examples=model.corpus_count, epochs=30, report_delay=1)

print('Nodes that are the most similar to node 0:')
for similarity in model.wv.most_similar(positive=['16']):
    print(f'   {similarity}')




