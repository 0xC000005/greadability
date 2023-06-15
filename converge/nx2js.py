import networkx as nx
import json

# Create a path graph with 10 nodes
G = nx.path_graph(10)

# Convert graph to dictionary
data = {
    "nodes": [{"name": str(node), "group": 1} for node in G.nodes()],
    "links": [{"source": str(edge[0]), "target": str(edge[1]), "value": 1} for edge in G.edges()]
}

# Save as JSON
with open("miserables.json", "w") as f:
    json.dump(data, f, indent=2)

if __name__ == '__main__':
    pass