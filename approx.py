import time
import networkx as nx

'''
This file holds the approximation algorithm for finding minimum vertex covers of graphs.
It creates a copy of the graph given (in networkx format) then picks an arbitrary edge of the graph
and adds it to the MVC. 
It then removes all adjacent edges to the above edge from the graph and continues this process.

This returns the MVC as a set C and a string that contains the trace file values.
'''

def MVC_approx(G):
    Gprime = G.copy()
    C = []
    stringval = ""
    start = time.time()
    while Gprime.edges():
        (u, v) = Gprime.edges()[0]
        C.append(u)
        C.append(v)
        for i in Gprime.neighbors(u):
            Gprime.remove_edge(u,i)
        for j in Gprime.neighbors(v):
            Gprime.remove_edge(v,j)
        stop = time.time() - start
        stringval += str(stop) + ", " + str(len(C)) + "\n"

    return C, stringval

