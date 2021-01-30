# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:27:55 2020
by Josh Limon
UID: 804-984-257
Network Visualization
Code modelled after tutorial by Abby Hickok
For classwork in Math 168 at UCLA Fall 2020
"""

import networkx as nx
import matplotlib.pyplot as plt

def plot_degree_dist(H):
    degrees = [H.degree(i) for i in H.nodes()]
    plt.hist(degrees, 20)
    plt.xticks([1, 2, 3, 4, 5])
    plt.xlabel('Degree')
    plt.ylabel('Nodes')
    plt.show()
    
def plot_eigenvector_centrality(H):
    centrality = nx.eigenvector_centrality(G)
    plt.figure(figsize=(10,3))
    plt.xlabel('Corresponding Node')
    plt.ylabel('Eigenvector Centrality')
    plt.bar(range(len(centrality)), list(centrality.values()), align='center')
    plt.xticks(range(len(centrality)), list(centrality.keys()))
    
def plot_betweenness_centrality(H):
    centrality = nx.betweenness_centrality(G)
    plt.figure(figsize=(10,3))
    plt.xlabel('Corresponding Node')
    plt.ylabel('Betweenness Centrality')
    plt.bar(range(len(centrality)), list(centrality.values()), align='center')
    plt.xticks(range(len(centrality)), list(centrality.keys()))

def plot_closeness_centrality(H):
    centrality = nx.closeness_centrality(G)
    plt.figure(figsize=(10,3))
    plt.xlabel('Corresponding Node')
    plt.ylabel('Closeness Centrality')
    plt.bar(range(len(centrality)), list(centrality.values()), align='center')
    plt.xticks(range(len(centrality)), list(centrality.keys()))    

file = open("russiantrade_edges.txt", "r")
lines = file.read().splitlines()
sources = [int(L.split('\t')[0]) for L in lines]
targets = [int(L.split('\t')[1]) for L in lines]
color_map = []
color_map.append('green')
E = len(sources)
color_map2 = []
color_map2.append('blue')

G = nx.Graph()
G.add_node(1, pos = (0.1, 0.95))
G.add_node(2, pos = (0.04, 0.565))
G.add_node(3, pos = (0.13, 0.52))
G.add_node(4, pos = (0.04, 0.04))
G.add_node(5, pos = (0.085, 0.15))
G.add_node(6, pos = (0.18, 0.21))
G.add_node(7, pos = (0.33, 0.185))
G.add_node(8, pos = (0.23, 0.35))
G.add_node(9, pos = (0.27, 0.32))
G.add_node(10, pos = (0.3, 0.42))
G.add_node(11, pos = (0.18, 0.515))
G.add_node(12, pos = (0.04, 0.525))
G.add_node(13, pos = (0.23, 0.68))
G.add_node(14, pos = (0.31, 0.75))
G.add_node(15, pos = (0.24, 0.83))
G.add_node(16, pos = (0.37, 0.78))
G.add_node(17, pos = (0.41, 0.83))
G.add_node(18, pos = (0.47, 0.85))
G.add_node(19, pos = (0.45, 0.80))
G.add_node(20, pos = (0.43, 0.745))
G.add_node(21, pos = (0.46, 0.72))
G.add_node(22, pos = (0.5, 0.72))
G.add_node(23, pos = (0.5, 0.69))
G.add_node(24, pos = (0.66, 0.725))
G.add_node(25, pos = (0.91, 0.625))
G.add_node(26, pos = (0.52, 0.49))
G.add_node(27, pos = (0.49, 0.46))
G.add_node(28, pos = (0.46, 0.38))
G.add_node(29, pos = (0.43, 0.283))
G.add_node(30, pos = (0.341, 0.36))
G.add_node(31, pos = (0.38, 0.445))
G.add_node(32, pos = (0.405, 0.43))
G.add_node(33, pos = (0.48, 0.51))
G.add_node(34, pos = (0.43, 0.56))
G.add_node(35, pos = (0.38, 0.63))
G.add_node(36, pos = (0.318, 0.6))
G.add_node(37, pos = (0.39, 0.72))
G.add_node(38, pos = (0.3, 0.66))
G.add_node(39, pos = (0.58, 0.625))
for i in range(E):
    G.add_edge(sources[i], targets[i])
    
    
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, node_color =color_map, edge_color = color_map2,  with_labels = True)

plot_eigenvector_centrality(G)
plot_betweenness_centrality(G)
plot_closeness_centrality(G)


"""pos = nx.spring_layout(G)
plt.figure(figsize = (50, 50))
nx.draw(G, pos, node_size = 30)
plt.show()"""

