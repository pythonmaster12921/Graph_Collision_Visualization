import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np



# Create the two separate graphs
G1 = nx.DiGraph()
G1.add_edges_from([('a', 'b'), ('b', 'c')])



G2 = nx.DiGraph()
G2.add_edges_from([('a', 'b'), ('b', 'd')])



# Set up the figure and the axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title('Collision of Two Graphs')



# Define the initial node positions as numpy arrays
pos1 = {'a': np.array([0, 0]), 'b': np.array([1, 0]), 'c': np.array([2, 0])}
pos2 = {'a': np.array([0, 1]), 'b': np.array([1, 1]), 'd': np.array([2, 1])}
pos = {**pos1, **pos2}



# Draw the initial state of the two separate graphs
nx.draw_networkx(G1, pos=pos1, node_color='lightblue', ax=ax)
nx.draw_networkx(G2, pos=pos2, node_color='lightgreen', ax=ax)



# Define the update function for the animation
def update(i):
# Define the position of the shared node for the current frame of the animation
    shared_pos = pos1['b'] + (i/10)*(pos2['b'] - pos1['b'])



    # Define the position of the fork nodes for the current frame of the animation
    if i < 5:
        fork_pos = shared_pos + (i/5)*(pos1['c'] - shared_pos)
    else:
        fork_pos = shared_pos + ((i-5)/5)*(pos2['d'] - shared_pos)

    print(i, fork_pos)

    # Clear the axis and draw the updated graph
    ax.clear()
    nx.draw_networkx_nodes(G, pos, nodelist=['a', 'b'], node_color='red', node_size=800, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=['c'], node_color='lightblue', node_size=800, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=['d'], node_color='lightgreen', node_size=800, ax=ax)
    nx.draw_networkx_edges(G, pos, ax=ax)



    # Draw a circle around the shared node
    circle = plt.Circle(shared_pos, 0.2, color='red', fill=False, lw=3)
    ax.add_patch(circle)



    # Draw a circle around the fork nodes
    circle = plt.Circle(fork_pos, 0.2, color='gray', fill=False, lw=3)
    ax.add_patch(circle)



# Create the combined graph
G = nx.DiGraph()
G.add_edges_from(G1.edges)
G.add_edges_from(G2.edges)



# Create the animation object
animation = FuncAnimation(fig, update, frames=20, interval=1000, repeat=False)



# Show the animation



# Show the animation
plt.show()