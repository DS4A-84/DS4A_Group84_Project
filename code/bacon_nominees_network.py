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




bacon_nodes_path = '../data/oracle_of_bacon_data/clean_data/nodes_year.csv'
bacon_edges_path = '../data/oracle_of_bacon_data/clean_data/edges_year.csv'

with open(bacon_edges_path, 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data


def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df

nodes = load_dataset(bacon_nodes_path)
#print(len(nodes))
#1146
edges = load_dataset(bacon_nodes_path)
#print(len(edges))
#45695

node_names = nodes['name']


def write_graph_info_per_year_csv(nodes, edges, year):
    
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    




for year in range(min(nodes.year),max(nodes.year)+1):
    nodes_sub = nodes[nodes.year == year]["name"]
    print(nodes_sub)
    edges_sub = edges[edges.year == year]["source","target"]
    edges_sub = [tuple(e) for e in edges_sub][1:] 
    node_names = nodes['name']
 
    print(edges_sub)
    exit()
    #write_graph_info_per_year_csv(nodes_sub,edges_sub)


'''
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
#density = nx.density(G)
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
'''
