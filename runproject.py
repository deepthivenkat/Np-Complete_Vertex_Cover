import argparse, os, time, sys
import networkx as nx
import os
import LS1, LS2, bnb_run, approx

"""
This is an executing funciton that will run the project for CSE 6140.
Arguments:
    -init:  the graph file to be read
    -alg:   the algorithm to be used (BnB, Approx, LS1, LS2)
    -time:  the time limit option for certain algorithms
    -seed:  the seed for certain algorithms

To call this in command line, type 'python runproject.py -init [arg1] -alg [arg2] -time [arg3] -seed [arg4]
Note that only the first two parameters are required for each algorithm
"""

# note that these will need to be changed for your directories

# inpath = os.getcwd() + '/'
outpath = os.getcwd() + "/"
#inpath = "/Users/Alex/Dropbox/College/Fall 2017/CSE 6140/project/Np-Complete_Vertex_Cover/"
#outpath = "/Users/Alex/Dropbox/College/Fall 2017/CSE 6140/project/Np-Complete_Vertex_Cover/results/"

parser = argparse.ArgumentParser(description='Run CSE 6140 project')
parser.add_argument('-inst', help='filename option')
parser.add_argument('-alg', help='algorithm option option')
parser.add_argument('-time', type=float, help='time limit option')
parser.add_argument('-seed', type=float, help='seed option')
args = parser.parse_args()

"""
This function creates a graph object from a file using networkx
"""
def makegraph(filename):
    graphfile = open(filename,'r')
    lines = graphfile.readlines()
    Vnum,Enum,n = lines[0].split()
    G = nx.Graph()
    for i, line in enumerate(lines):
        if i != 0:
            vals = line.split()
            for j in vals:
                G.add_edge(int(i),int(j))
    return G

G = makegraph(args.inst)

if (args.alg == 'BnB'):
    clipinst = args.inst
    # LS1.Local_Search(G, args.time)
    outputsol = '%s_%s_%s.sol' % (clipinst.split("/")[-1][:-6], args.alg,str(int(args.time)))
    outputtrace = '%s_%s_%s.trace' % (clipinst.split("/")[-1][:-6], args.alg,str(int(args.time)))
    sol, trace = bnb_run.bnb_main(G, args.time, outputsol, outputtrace)
    # print outpath + outputsol
    output1 = open(outpath + outputsol,'w')
    output1.write(str(len(sol))+"\n")
    sol = [str(item) for item in sol]
    output1.write(",".join(sol))
    output1.close()
    output2 = open(outpath + outputtrace,'w')
    for line in trace:
        output2.write(line)
        output2.write("\n")
    output2.close()

elif (args.alg == 'Approx'):
    # sys.exit('Error')
    clipinst = args.inst
    sol,trace = approx.MVC_approx(G)
    outputsol = '%s_%s.sol' % (clipinst.split("/")[-1][:-6], args.alg)
    outputtrace = '%s_%s.trace' % (clipinst.split("/")[-1][:-6], args.alg)
    output1 = open(outpath + outputsol,'w')
    output1.write(str(len(sol))+"\n")
    solstring = ""
    for i in sol:
        solstring += str(i) + ","
    output1.write(solstring[:-1])
    output1.close()
    output2 = open(outpath + outputtrace,'w')
    output2.write(trace)
    output2.close()

elif (args.alg =='LS1'):
    clipinst = args.inst
    # LS1.Local_Search(G, args.time)
    sol,trace = LS1.Local_Search(G, args.time)
    outputsol = '%s_%s_%s_%s.sol' % (clipinst.split("/")[-1][:-6], args.alg,str(int(args.time)),str(int(args.seed)))
    outputtrace = '%s_%s_%s_%s.trace' % (clipinst.split("/")[-1][:-6], args.alg,str(int(args.time)),str(int(args.seed)))
    print outpath + outputsol
    output1 = open(outpath + outputsol,'w')
    # output1.write(str(len(sol))+"\n")
    output1.write(sol)
    output1.close()
    output2 = open(outpath + outputtrace,'w')
    output2.write(trace)
    output2.close()

elif (args.alg == 'LS2'):
    clipinst = args.inst
    # LS1.Local_Search(G, args.time)
    sol,trace = LS2.Local_Search(G, args.time)
    outputsol = '%s_%s_%s_%s.sol' % (clipinst.split("/")[-1][:-6], args.alg,str(int(args.time)),str(int(args.seed)))
    outputtrace = '%s_%s_%s_%s.trace' % (clipinst.split("/")[-1][:-6], args.alg,str(int(args.time)),str(int(args.seed)))
    output1 = open(outpath + outputsol,'w')
    # output1.write(str(len(sol))+"\n")
    output1.write(sol)
    output1.close()
    output2 = open(outpath + outputtrace,'w')
    output2.write(trace)
    output2.close()

else:
    sys.exit('Error')

