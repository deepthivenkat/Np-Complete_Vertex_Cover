import time
import random
import networkx as nx
from collections import defaultdict
G = nx.Graph()


# def build_adjacency_list(f):
	# adj_list = defaultdict(list)
	
def ConstructRandomVC(G,k):
	VC_size_k = []
	nodes_list = G.nodes()
	try:
		idx_vertices = random.sample(range(0,len(nodes_list)),k)
	except ValueError:
		print "No of vertices needed is greater than the total number of vertices"
	for idx in idx_vertices:
		VC_size_k.append(nodes_list[idx])
	return VC_size_k

def Local_Search(G, vertex_count, edge_count):
	gain_list = {}
	for vertex in G.nodes():
		gain_list[vertex] = len(G.neighbors(vertex))
	# print gain_list
	k = random.randint(1,len(G.nodes()))
	i = 10000
	random_VC_k = ConstructRandomVC(G,k)
	while i:
		i -= 1
		edges_covered_by_vertices = 0
		edge_set = set()
		for vrtx in random_VC_k:
			for neigh_edges in G.neighbors(vrtx):
				edge_set.add(neigh_edges)
		edges_covered_by_vertices += len(list(edge_set))
		current_gain = [gain_list[vtx] for vtx in random_VC_k]
		if edges_covered_by_vertices == edge_count:
			min_gain_idx = current_gain.index(min(current_gain))
			min_gain_vrtx = random_VC_k[min_gain_idx]
			random_VC_k.remove(min_gain_vrtx)
			continue 
		uncovered_edges = list(set(G.edges()) - edge_set)
		random_uncovered_edge_index = random.randint(1,len(G.nodes()))
		random_uncovered_edge = uncovered_edges[random_uncovered_edge_index]
		end_pt_1 = random_uncovered_edge[0]
		end_pt_2 = random_uncovered_edge[1]
		if len(G.neighbors(end_pt_1)) > len(G.neighbors(end_pt_2)):
			random_VC_k += [end_pt_1]
		else:
			random_VC_k += [end_pt_2]
		random_VC_k = list(set(random_VC_k))
		print "current iteration VC length", len(random_VC_k)
	return random_VC_k




f = open("jazz.graph")
V_E_D = f.readline()
Vertices, Edges, Directed = map(int,(V_E_D.split(" ")))
G.add_nodes_from(range(1,Vertices+1))
for idx,line in enumerate(f):
		adj_edges = map(int,line.split(" ")[:-1])
		source_edges = [idx+1] * len(adj_edges)
		# print adj_edges
		G.add_edges_from(zip(source_edges,adj_edges))
VC_LS = Local_Search(G,Vertices,Edges)
print VC_LS,len(VC_LS)


