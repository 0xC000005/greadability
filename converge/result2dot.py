import networkx as nx
import matplotlib.pyplot as plt
import json

# Load the layout.json under the current folder
with open("layout.json", "r") as f:
    data = json.load(f)

# Create a new graph
G = nx.Graph()

# Add nodes with their attributes to the graph
pos = {}
for node_data in data:
    G.add_node(node_data["name"], x=node_data["x"], y=node_data["y"])
    pos[node_data["name"]] = (node_data["x"], node_data["y"])

# Write the graph to a .dot file
nx.drawing.nx_agraph.write_dot(G, "graph.dot")

# Draw the graph using the positions from layout.json
nx.draw(G, pos, with_labels=True)
plt.show()

if __name__ == '__main__':
    pass