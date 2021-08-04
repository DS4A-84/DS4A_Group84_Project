#!/usr/bin/python

# DS4A Project
# Group 84
# using node/edge info to create network graph
# and do social network analysis

import csv
import networkx as nx
from networkx.algorithms import community
from operator import itemgetter
from os import path
import pandas as pd
import plotly.offline as py
import plotly.graph_objects as go


degree_df_path = '../../data/imbd_data/network_degree_data.csv'
nodes_df_path = '../../data/imbd_data/nodes.csv'
edges_df_path = '../../data/imbd_data/edges.csv'



def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df



def write_graph_info_per_year_csv(nodes, edges, year, filepath):
    
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    # Get Centrality
    # degree is simplest/common way to find important nodes, nodes degree is sum of its edges
    degree_dict = dict(G.degree(G.nodes()))
    nx.set_node_attributes(G, degree_dict, 'degree')
    sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
    sorted_degree = pd.DataFrame(sorted_degree,columns=["nconst","degree"])
    sorted_degree["year"] = year

    #write data to csv
    # if no csv exists
    if not path.exists(filepath):
        sorted_degree.to_csv(filepath,index=False)
    else:
        sorted_degree.to_csv(filepath, mode='a', header=False,index=False)    


# MAIN
nodes = load_dataset(nodes_df_path)
#print(len(nodes))
#1753164
edges = load_dataset(edges_df_path)
#print(len(edges))
#16893288

#print(nodes.head(1))
#print(edges.head(1))
#print(max(nodes.film_year.unique()))
#print(min(nodes.film_year.unique()))
#print(max(edges.year.unique()))
#print(min(edges.year.unique()))
#edges begin in 1892, pointing to multi actor/actress movies started at this time

'''
      nconst  film_year
0  nm0000001       1934
      source     target  year
0  nm0005690  nm0374658  1892
'''




for year in range(min(edges.year),max(edges.year)+1):
    nodes_sub = nodes[nodes.film_year <= year]["nconst"]
    edges_sub = edges[edges.year <= year]
    edges_sub = edges_sub[["source","target"]]
    edges_sub = list(zip(edges_sub.source, edges_sub.target)) 

    write_graph_info_per_year_csv(nodes_sub,edges_sub,year,degree_df_path)

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
