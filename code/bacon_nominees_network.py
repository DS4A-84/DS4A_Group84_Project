#!/usr/bin/python

# DS4A Project
# Group 84
# using node/edge info to create network graph
# and do social network analysis

import csv
import networkx as nx
from networkx.algorithms import community
from operator import itemgetter
import pandas as pd
import plotly.offline as py
import plotly.graph_objects as go




bacon_nodes_path = '../data/oracle_of_bacon_data/clean_data/bacon_nodes.csv'
bacon_edges_path = '../data/oracle_of_bacon_data/clean_data/bacon_edges.csv'

'''
with open(bacon_nodes_path, 'r') as nodecsv:
    nodereader = csv.reader(nodecsv)
    nodes = [n for n in nodereader][1:]

node_names = [n[0] for n in nodes]


with open(bacon_edges_path, 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data
'''

def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df

nodes = load_dataset(bacon_nodes_path)
#print(len(nodes))
#1146


with open(bacon_edges_path, 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data
#print(len(edges))
#45695

node_names = nodes['name']

G = nx.Graph()

G.add_nodes_from(node_names)
G.add_edges_from(edges)
print(nx.info(G))
#Name:
#Type: Graph
#Number of nodes: 1167
#Number of edges: 35031
#Average degree:  60.0360



# Get network density
density = nx.density(G)
print("Network density:", density)
#Network density: 0.051488841953022
# This is not a very dense network on a scale from 0-1

# Get network largest component
print(nx.is_connected(G))
components = nx.connected_components(G)
largest_component = max(components, key=len)

# Get network diameter based on largest component
subgraph = G.subgraph(largest_component)
diameter = nx.diameter(subgraph)
print("Network diameter of largest component:", diameter)
#Network diameter of largest component: 6


# Get triadic closure, measure it via clustering coefficient or transitivity
# transitibity is the ratio of all triangles over all possible triangles.
triadic_closure = nx.transitivity(G)
print("Triadic closure:", triadic_closure)

# Get Centrality
# degree is simplest/common way to find important nodes, nodes degree is sum of its edges
degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degree')
sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)


# print top 20 highest degree
print("Top 20 nodes by degree:")
for d in sorted_degree[:20]:
    print(d)

