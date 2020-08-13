# https://networkx.github.io/documentation/stable/tutorial.html

import networkx as nx
import matplotlib.pyplot as plt

##### Creating a graph

G = nx.Graph()
# By definition, a Graph is a collection of nodes (vertices) along with identified pairs of nodes (called edges, links, etc). In NetworkX, nodes can be any hashable object e.g., a text string, an image, an XML object, another Graph, a customized node object, etc.

##### Nodes

# add one node at a time
G.add_node(1)

# add a list of nodes
G.add_nodes_from([2, 3])

# or add any iterable container of nodes
H = nx.path_graph(10)
G.add_nodes_from(H)
# Note that G now contains the nodes of H as nodes of G.

# In contrast, you could use the graph H as a node in G.
G.add_node(H)

# both print nothing
print(G)
print(H)

##### Edges

# G can also be grown by adding one edge at a time
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e) # unpack edge tuple*
# by adding a list of edges
G.add_edges_from([(1, 2), (1, 3)])

G.add_edges_from(H.edges)

# remove all nodes and edges
G.clear()

# add new nodes/edges quitely ignores any that are already present
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam") # adds node "spam"
G.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

print("G.number_of_nodes()": G.number_of_nodes())
print("G.number_of_edges()": G.number_of_edges())

print("\nlist(G.nodes)", list(G.nodes))
# [1, 2, 3, 'spam', 's', 'p', 'a', 'm']

##### Drawing graphs

