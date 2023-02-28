# importing networkx
import networkx as nx
 
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

G1 = nx.DiGraph()
G1.add_edges_from([('a', 'b'), ('b', 'c')])
 
nx.draw(G1)
# plt.savefig("filename.png")
plt.show()