import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True)
plt.show()

stopien_centralnosci = nx.degree_centrality(G)
print(stopien_centralnosci)

posrednictwo = nx.betweenness_centrality(G)
print(posrednictwo)

bliskosc = nx.closeness_centrality(G)
print(bliskosc)

centrality = nx.eigenvector_centrality(G)
print(centrality)

