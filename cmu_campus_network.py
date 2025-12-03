"""
NetworkX Hello World Project

1. Create a graph network
2. Add nodes and weighted edges
3. Find shortest paths
4. Analyze network properties
5. Visualize the network

TODO: Fill in the missing code sections
"""

import networkx as nx
import matplotlib.pyplot as plt

# ============================================================================
# PART 1: Create the Graph
# ============================================================================
print("Part 1: Creating the graph...")

# Create an undirected graph
G = nx.Graph()

# CMU Buildings - we'll keep this simple with just 5 buildings
buildings = [
    'Gates Hillman Center',
    'Wean Hall',
    'Hunt Library',
    'Cohon Center',
    'Tepper Building'
]

# Add buildings as nodes
G.add_nodes_from(buildings)

print(f"Added {G.number_of_nodes()} buildings to the network")

# ============================================================================
# PART 2: Add Walking Paths with Times
# ============================================================================
print("\nPart 2: Adding walking paths...")

# Walking paths between buildings with estimated times in minutes
# Format: (building1, building2, walking_time_minutes)
paths = [
    ('Gates Hillman Center', 'Wean Hall', 2),
    ('Wean Hall', 'Hunt Library', 3),
    ('Hunt Library', 'Cohon Center', 2),
    ('Cohon Center', 'Tepper Building', 1),
    ('Tepper Building', 'Gates Hillman Center', 2),
    ('Wean Hall', 'Cohon Center', 4)  # Alternative longer path
]

# Add the paths as weighted edges
for building1, building2, time in paths:
    G.add_edge(building1, building2, weight=time)

print(f"Added {G.number_of_edges()} walking paths")

# ============================================================================
# PART 3: Find Shortest Path
# ============================================================================
print("Part 3: Finding shortest paths...")

start = 'Gates Hillman Center'
end = 'Hunt Library'

# Find the shortest route (by weight)
shortest_path = nx.shortest_path(G, source=start, target=end, weight='weight')

# Find the walking time
walking_time = nx.shortest_path_length(G, source=start, target=end, weight='weight')

print(f"\nShortest route from {start} to {end}:")
print(f"  Route: {' -> '.join(shortest_path)}")
print(f"  Walking time: {walking_time} minutes")

# ============================================================================
# PART 4: Network Analysis
# ============================================================================
print("Part 4: Analyzing the network...")

print("\nConnections per building:")
for building in G.nodes():
    degree = G.degree(building)
    print(f"  {building:25s}: {degree} connections")

# Betweenness centrality
betweenness = nx.betweenness_centrality(G, weight='weight')
most_central = max(betweenness, key=betweenness.get)
print(f"\nMost central building: {most_central}")

# ============================================================================
# Part 6: Harder Challenges (Pick 1 Challenge)
# ============================================================================

# 1. ALL possible paths
print("\n1. Find ALL possible paths from Gates Hillman Center to Hunt Library:")
all_paths = list(nx.all_simple_paths(G, start, end))
for p in all_paths:
    print("  " + " -> ".join(p))

# 2. If Wean Hall is closed
print("\n2. What if Wean Hall is closed for construction?")
G_closed = G.copy()
G_closed.remove_node('Wean Hall')

try:
    alt_path = nx.shortest_path(G_closed, start, end, weight='weight')
    alt_time = nx.shortest_path_length(G_closed, start, end, weight='weight')
    print(f"  New shortest path: {' -> '.join(alt_path)}")
    print(f"  Walking time: {alt_time} minutes")
except nx.NetworkXNoPath:
    print("  No available path without Wean Hall.")

# 3. Average walking time
print("\n3. Calculate the average walking time between any two buildings:")
avg_time = nx.average_shortest_path_length(G, weight='weight')
print(f"  Average walking time: {avg_time:.2f} minutes")
