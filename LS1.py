import time
import random
import networkx as nx
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import repeat
import math

	
def ConstructRandomVC(G,k, gain_list):
	sorted_gain_k = sorted(gain_list.items(), key=lambda x:x[1],reverse=True)[:k]
	VC_size_k = [v[0] for v in sorted_gain_k]
	return VC_size_k


def Local_Search(G, vertex_count=0, edge_count=0):
	vertex_count=len(G.nodes())
	edge_count = len(G.edges())
	gain_list = {}
	for vertex in G.nodes():
		gain_list[vertex] = len(G.neighbors(vertex))
	k = int(.65*vertex_count)
	start = time.time()
	iter_no = 0
	random_VC_k = ConstructRandomVC(G,k,gain_list)
	most_optimal_VS_so_far = []
	VC_obtained = []
	min_VC_len = float("inf")
	soln_found = False
	adj_mat = [[0 for i in range(vertex_count)] for i in range(vertex_count)]
	edges_covered_by_vertices = 0
	covered_edges = defaultdict(int)
	for vrtx in random_VC_k:
		for neigh_edges in nx.edges(G,vrtx):
			u,v = neigh_edges
			if v < u:
				neigh_edges=(v,u)
			covered_edges[neigh_edges] += 1
	uncovered_edges = defaultdict(int)
	uncovered_edges_list = list(set(G.edges()) - set(covered_edges.keys()))
	uncovered_edges = dict(zip(uncovered_edges_list,repeat(1)))
	edges_covered_by_vertices = len(covered_edges)
	double_vertex_edges = [k for k,v in covered_edges.iteritems() if v == max(covered_edges.values())]
	while time.time()-start <= 600:
		edges_covered_by_vertices = len(covered_edges)
		iter_no += 1
		soln_length = len(random_VC_k)
		if edges_covered_by_vertices == edge_count:
			soln_found = True
			VC_obtained = random_VC_k
			if soln_length <= min_VC_len:
				min_VC_len = soln_length
				most_optimal_VS_so_far = tuple(random_VC_k)
				print time.time()-start, soln_length
			range_var = soln_length/10
			if range_var < 5:
				range_var = 10
			for i in range(1,range_var):
				if double_vertex_edges:
					removing_edgs = random.choice(double_vertex_edges)
					vrtx1,vrtx2 = removing_edgs 
					if gain_list[vrtx1] > gain_list[vrtx2]:
						removing_vert = vrtx1
					else:
						removing_vert = vrtx2
					random_VC_k.remove(removing_vert)
					for n in nx.edges(G,removing_vert):
							p,q = n
							if q<p:
								n = (q,p)
							covered_edges[n] -= 1
							try:
								double_vertex_edges.remove(n)
							except ValueError, AttributeError:
								pass
							if covered_edges[n] <= 0:
								del covered_edges[n]
								uncovered_edges[n] = 1
			continue 
		random_uncovered_edge = random.choice(uncovered_edges.keys())
		end_pt_1 = random_uncovered_edge[0]
		end_pt_2 = random_uncovered_edge[1]
		if len(G.neighbors(end_pt_1)) > len(G.neighbors(end_pt_2)):
			random_VC_k.append(end_pt_1)
			for nei in nx.edges(G,end_pt_1):
				k,l = nei
				if l<k:
					nei = (l,k)
				covered_edges[nei] += 1
				if covered_edges[nei] == 2:
					double_vertex_edges.append(nei)
				uncovered_edges.pop(nei,None)
		else:
			random_VC_k.append(end_pt_2)
			for nei in nx.edges(G,end_pt_2):
				k,l = nei
				if l<k:
					nei = (l,k)
				covered_edges[nei] += 1
				if covered_edges[nei] == 2:
					double_vertex_edges.append(nei)
				uncovered_edges.pop(nei,None)
		random_VC_k = list(set(random_VC_k))
	if not soln_found:
		print edges_covered_by_vertices,len(G.edges()), time.time()-start
	return most_optimal_VS_so_far 



"""
f = open("star.graph")
G = nx.Graph()
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
"""

