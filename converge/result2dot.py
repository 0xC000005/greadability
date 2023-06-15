import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import json

# Load the dolphin edges csv file
df = pd.read_csv('../../netviz/sample_graphs/dolphins-edges.csv')
df['~from'] = df['~from'].str.replace('n', '')
df['~from'] = df['~from'].astype(int)
df['~to'] = df['~to'].str.replace('n', '')
df['~to'] = df['~to'].astype(int)

# Create a graph using edge data
G = nx.from_pandas_edgelist(df, source='~from', target='~to', create_using=nx.Graph())

# Load the layout.json under the current folder
with open("layout.json", "r") as f:
    data = json.load(f)

# Add node positions to the graph
pos = {}
for node_data in data:
    G.add_node(node_data["name"], x=node_data["x"], y=node_data["y"])
    pos[node_data["name"]] = np.array([node_data["x"], node_data["y"]])

print(pos)

# Write the graph to a .dot file
nx.drawing.nx_agraph.write_dot(G, "graph.dot")

# Draw the graph
nx.draw(G, pos=pos, with_labels=True)
# save the graph as a png file
plt.savefig("graph.png")
