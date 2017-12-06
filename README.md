# Np-Complete_Vertex_Cover Group 31

This code is written by Alexander, Junlin, and Deepthi for the CSE 6140 project. It solves for the minimum vertex cover of a given graph file and returns a solution file containing the MVC and a trace file containing how the algorithm worked over time.

## To use

To run this code, call 
```
python runproject -inst <file> -alg [BnB | LS1 | LS2 | Approx] -time <cutofftime> -seed <randomseed>
```

where BnB is branch and bound, LS1 is local search 1 using a hill climbing strategy, LS2 is local search 2 using a vertex removal strategy, and Approx is the approximation algorithm. 

### Prerequisites

To use the code, you need a copy of Python. The following libraries are used:
* time
* random
* networkx
* collections
* itertools
* math
* os
* copy
* argparse
* sys
Make sure these are available in order to have the code run smoothly.

## Algorithms

There are four algorithms used in this project:

### Branch and Bound

This algorithm takes in four inputs:
* A graph
* A time cutoff
* A solultion file
* A trace file

It then fills the files with the corresponding result and traces for a given graph.

### LS1

This local search algorithm uses a hill climbing strategy to solve for the MVC.
It requires the following inputs:
* A graph
* A time cutoff
* A random seed

### LS2

This local search algorithm removes edges from the graph that are adjacent to edges in the vertex cover.
It requires the following inputs:
* A graph
* A time cutoff
* A random seed

### Approximation

This is an approximation algorithm that repeatidly adds an arbitrary edge of the graph to the vertex cover, then removes all adjacent edges from the graph.
It requires the following inputs:
* A graph

