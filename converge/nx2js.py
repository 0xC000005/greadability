import networkx as nx
import json
import pandas as pd

# Create a path graph with 10 nodes
df = pd.read_csv(r'C:\Users\0xc00\OneDrive\Documents\netviz\sample_graphs\price_10000nodes-edges.csv')
df['~from'] = df['~from'].str.replace('n', '')
# convert every element to int
df['~from'] = df['~from'].astype(int)
df['~to'] = df['~to'].str.replace('n', '')
df['~to'] = df['~to'].astype(int)
G = nx.from_pandas_edgelist(df, source='~from', target='~to', create_using=nx.Graph())

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