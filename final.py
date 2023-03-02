import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Create the two separate graphs
G1 = nx.DiGraph()
G1.add_edges_from([('a', 'b'), ('b', 'c'), ('a', 'e')])
G2 = nx.DiGraph()
G2.add_edges_from([('a', 'b'), ('b', 'd')])

# Define the initial node positions as numpy arrays
pos1 = {'a': np.array([0, 0]), 'b': np.array([1, 0]), 'c': np.array([2, 0]), 'e': np.array([3, 0.5])}
pos2 = {'a': np.array([0, 1]), 'b': np.array([1, 1]), 'd': np.array([2, 1])}
pos = {**pos1, **pos2}

# Merge the seperate graphs
G = nx.DiGraph()
G.add_edges_from(G1.edges)
G.add_edges_from(G2.edges)

# Get the list of merged graph edges
animated_edge = []
G_draw_list = []
for edge in G.edges:
    G_draw = nx.DiGraph()
    animated_edge.append(edge)
    G_draw.add_edges_from(animated_edge)
    G_draw_list.append(G_draw)

# Get the total number of updates in the merged graph
edgeNum = len(G_draw_list)

# Set up the figure and the axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title('Collision of Two Graphs')

# Draw the initial state of the two separate graphs
nx.draw_networkx(G1, pos=pos1, node_color='lightblue', ax=ax)
nx.draw_networkx(G2, pos=pos2, node_color='lightgreen', ax=ax)

# Get the original limit of the axes
xLim = ax.get_xlim()
yLim = ax.get_ylim()

# Update the graph
def update(i):
    if i > 0:
        ax.clear()
        ax.set_xlim(xLim)
        ax.set_ylim(yLim)
        nx.draw_networkx(G_draw_list[i-1], pos=pos, node_color='lightgreen', ax=ax)

# Create the animation object
animation = FuncAnimation(fig, update, frames=edgeNum+1, interval=1500, repeat=False)

# Show the animation
plt.show()