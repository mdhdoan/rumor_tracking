import networkx

nx = networkx
file = 'higgs-retweet_network.edgelist'
filename = open(file, 'rb')
print(type(filename))
graph_data = nx.read_edgelist(filename, nodetype = int, create_using=nx.DiGraph) 
print(graph_data.nodes())
filename.close()