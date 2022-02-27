import networkx as nx
import matplotlib.pyplot as plt
import random

g = nx.Graph()
g.add_nodes_from(range(1,20))

for i in g.nodes():
    for j in g.nodes():
        if (i < j):
            rnd = random.random()
            if rnd < 0.03:
                g.add_edge(i, j)
    pos = nx.random_layout(g)

nx.draw(g, pos, with_labels = 1)
plt.show()