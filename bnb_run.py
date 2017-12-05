import networkx as nx
from copy import deepcopy
from time import time
import os

'''
This file is to implement the branch and bound algorithom for the minimum vertex cover problem.
The main function reads the graph file and pass the data to the bnb function.
The bnb function is the main body of the algorithm.
The LowerBound function calculates the the lower bound that is required in the branch and bound algorithm.
'''

'''
LowerBound: Calculates the the lower bound of the branch and bound algorithm.
Inputs: G: the sub-graph generated in a recursion
Here we implement three lower bounds. (the latter two are commented)
The first one generates a maximal matching and use its length as a lower bound.
The second one just ignore the lower bound and return 0.
The third one generates a maximum matching and use its length as a lower bound.
Default is the first one.
'''
def LowerBound(G):

    # The first lower bound. Default. Tested to be the best among the three.
    LB = 0
    tempG = deepcopy(G)
    while tempG.edges() != []:
        edge = tempG.edges().pop()
        tempG.remove_nodes_from([edge[0],edge[1]])
        LB = LB + 1
    return LB

    # The second lower bound. Tested to be much slower that the first one.
    # return 0

    # The third lower bound.  Supposed to be the tightest but slow to calculate. Performed badly during tests.
    # return len(nx.max_weight_matching(G)) / 2

'''
bnb: Main body of the algorithm.
Inputs: v: node number of the original graph. index: the first node index of the sub-graph in a recursion
result: partial result for the sub-graph. thisG: the sub-graph. minSoFar: temporary final result list.
startTime: start time used in timing. timeOut: user input to decide when to exit. outputFile/traceFile: user input of files.
'''

def bnb(v, index, result, thisG, minSoFar, startTime, timeOut, trace):

    # if timeout, output and exit.
    if time() - startTime > timeOut:
        raise RuntimeError

    # prune this branch of reach the lower bound
    if len(result) + LowerBound(thisG) >= len(minSoFar):
        return
    # if a result is not pruned and comes to a complete result, refresh the new minSoFar
    elif thisG.edges() == []:
        del minSoFar[:]
        for i in result:
            minSoFar.append(i)
        # trace it in the output files
        print (("%.2f" % (time() - startTime)) + "," + str(len(minSoFar)))
        trace.append(("%.2f" % (time() - startTime)) + "," + str(len(minSoFar)))
        return

    # further our result to all nest node
    for i in range(index, v + 1):
        # prune if the node is useless
        if i not in thisG.nodes():
            continue
        # recursion
        result.append(i)
        tempG = deepcopy(thisG)
        tempG.remove_node(i)
        bnb(v, i + 1, result, tempG, minSoFar, startTime, timeOut, trace)
        del result[-1]

def bnb_main(G,cutoff, outputSolFileName, outputTraceFileName):
    trace = []
    minSoFar = G.nodes()
    v = len(minSoFar)
    index = 1
    result = []
    timeOut = cutoff
    startTime = time()
    try:
        bnb(v, index, result, G, minSoFar, startTime, timeOut, trace)
    except RuntimeError:
        print "Timeout. Returned best solution so far."
    return minSoFar, trace

    
    

'''
main: User input and other miscellaneous stuff
# '''
# def main():
    
#     # user inputs
#     fileName = "karate.graph"
#     timeOut = 10 # in seconds
#     outputFileName = "output.sol"
#     traceFileName = "trace.trace"
    
#     # read graph into memory
#     with open(fileName,"r") as graphData:
#         v, e, zero = map(lambda x : int(x), graphData.readline().split())
#         G = nx.Graph()
#         G.add_nodes_from(range(1, v + 1))
#         for i in range(v):
#             G.add_edges_from(map(lambda x : (i + 1, int(x)), graphData.readline().split()))
#     graphData.close()

#     # sample small graph for debugging
#     # G = nx.Graph()
#     # G.add_nodes_from(range(1,7))
#     # G.add_edges_from([(1,2),(2,3),(1,4),(3,5),(2,6),(6,7),(6,8),(7,8)])
#     # v = len(G.nodes())
    
#     # initialize variables
#     index = 1
#     result = []
#     minSoFar = G.nodes()
#     startTime = time()
    
#     # write data into output files
#     with open(outputFileName, "w") as outputFile:
#         with open(traceFileName, "w") as traceFile:
#             try:
#                 bnb(v, index, result, G, minSoFar, startTime, timeOut, outputFile, traceFile)
# 		outputFile.write(str(len(minSoFar)))
#                 outputFile.write("\n")
#                 outputFile.write(",".join(map(lambda x : str(x), minSoFar)))
#                 outputFile.write("\n")
#             except RuntimeError:
#                 print "Timeout. Returned best solution so far."
#     traceFile.close()
#     outputFile.close()

# # run the code
# if __name__ == "__main__":
#     main()
