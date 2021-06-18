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




bacon_nodes_path = 'data/bacon_nodes.csv'
bacon_edges_path = 'data/bacon_edges.csv'

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


with open(bacon_edges_path, 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data


node_names = nodes['name']

G = nx.Graph()

G.add_nodes_from(node_names)
G.add_edges_from(edges)

print(nx.info(G))
