import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

#Helper function to calculate the average
def average(lst):
    return sum(lst)/len(lst)

#Function to plot the degree distribution using the degrees.
def plot_deg_dist(graphs, c, n, p):
    fig = plt.figure()
    for g in graphs:
        degrees = [d for n, d in g.degree()]
        plt.plot(*np.unique(degrees, return_counts = True))
        plt.xlabel("Degrees")
        plt.ylabel("No. of Nodes")
        plt.suptitle("Average Degree Distribution of an E-R Network")
        plt.title("Expected degree distribution is " + str((n-1)*p))
    filename = f'CS363-HW-02/graphs/configuration{c}.png'
    plt.savefig(filename)

#Function to generate i E-R networks
def er_generator(n, p, i):
    er_graphs = []

    for _ in range(i):
        er_graphs.append(nx.fast_gnp_random_graph(n, p, seed = np.random))
    
    return er_graphs

#Function to return the list of average degree, clustering coefficient, and apl of the graphs of the given config
def er_analyzer(er_graphs):
    avg_deg = []
    avg_cc = []
    avg_apl = []

    for graph in er_graphs:
        deg = [edge[1] for edge in graph.degree()]
        avg_deg.append(sum(deg)/len(deg))
        avg_cc.append(nx.average_clustering(graph))
        avg_apl.append(nx.average_shortest_path_length(graph))
    
    return avg_deg, avg_cc, avg_apl


#Driver Code
configs = [ (400, 0.2), (1000, 0.03), (1500, 0.04)]
i = 30
c = 1

for n, p in configs:
    er_graphs = er_generator(n, p, i)
    avg_deg, avg_cc, avg_apl = er_analyzer(er_graphs)

    print("******* configuration: n = ", n, ", p = ", p, " *******")
    print("Average degree is ", average(avg_deg))
    print("Average clustering coefficient is ", average(avg_cc))
    print("Average path lenght is ", average(avg_apl), '\n')

    chosen_graphs = [random.randint(0, i-1) for _ in range(5)]
    chosen_graphs_list = [er_graphs[x] for x in chosen_graphs]
    plot_deg_dist(chosen_graphs_list, c, n, p)
    c += 1