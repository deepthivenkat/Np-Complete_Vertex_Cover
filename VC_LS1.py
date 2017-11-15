import time
import random
import networkx as nx
from collections import defaultdict
from collections import Counter
from collections import deque


# def build_adjacency_list(f):
	# adj_list = defaultdict(list)
	
def ConstructRandomVC(G,k, gain_list):
	sorted_gain_k = sorted(gain_list.items(), key=lambda x:x[1],reverse=True)[:k]
	VC_size_k = [v[0] for v in sorted_gain_k]
	return VC_size_k
	# nodes_list = G.nodes()
	# try:
	# 	idx_vertices = random.sample(range(0,len(nodes_list)),k)
	# except ValueError:
	# 	print "No of vertices needed is greater than the total number of vertices"
	# for idx in idx_vertices:
	# 	VC_size_k.append(nodes_list[idx])
	# return VC_size_k

def Local_Search(G, vertex_count=0, edge_count=0):
	vertex_count=len(G.nodes())
	edge_count = len(G.edges())
	gain_list = {}
	for vertex in G.nodes():
		gain_list[vertex] = len(G.neighbors(vertex))
	# print gain_list
	k = vertex_count/2
	iter_no = 1000
	random_VC_k = ConstructRandomVC(G,k,gain_list)
	most_optimal_VS_so_far = []
	VC_obtained = []
	prev_VC_len = deque([],200)
	while iter_no:
		print "iteration number ",iter_no
		iter_no -= 1
		adj_mat = [[0 for i in range(vertex_count)] for i in range(vertex_count)]
		edges_covered_by_vertices = 0
		edge_set = set()
		for vrtx in random_VC_k:
			# for neigh_edges in G.neighbors(vrtx):
			for neigh_edges in nx.edges(G,vrtx):
				u,v = neigh_edges
				adj_mat[u-1][v-1] = 1
				adj_mat[v-1][u-1] = 1
				# if (u,v) not in edge_set and (v,u) not in edge_set:
				edge_set.add(neigh_edges)
		# edges_covered_by_vertices += len(list(edge_set))
		edges_covered_by_vertices += sum(sum(x) for x in adj_mat)/2
		# print "Edges covered by VC: ", edges_covered_by_vertices, "Edge count", edge_count
		current_gain = [gain_list[vtx] for vtx in random_VC_k]
		if edges_covered_by_vertices == edge_count:
			VC_obtained = random_VC_k
			prev_VC_len.append(len(random_VC_k))
			if len(random_VC_k) == min(prev_VC_len):
				print "minimum obtained so far", len(random_VC_k), min(prev_VC_len)
				most_optimal_VS_so_far = random_VC_k
			# print "#"*200
			# print 'deque',prev_VC_len
			if Counter(prev_VC_len).most_common(1)[0][1] == 150:
				return most_optimal_VS_so_far
			# min_gain_idx = current_gain.index(min(current_gain))
			# min_gain_vrtx = random_VC_k[min_gain_idx]
			removing_vert = random.choice(random_VC_k)
			random_VC_k.remove(removing_vert)
			print "Stabilized!"*40, "removing ", removing_vert
			# print [x for x in G.edges() if x not in edge_set]
			continue 
		uncovered_edges = list(set(G.edges()) - edge_set)
		# print uncovered_edges, "*"*200
		# print edge_set, "*"*200
		# print random_VC_k
		# random_uncovered_edge_index = random.randint(1,len(G.nodes()))
		random_uncovered_edge = random.choice(uncovered_edges)
		end_pt_1 = random_uncovered_edge[0]
		end_pt_2 = random_uncovered_edge[1]
		if len(G.neighbors(end_pt_1)) > len(G.neighbors(end_pt_2)):
			random_VC_k.append(end_pt_1)
			# print "Adding new edge endp1", end_pt_1
		else:
			random_VC_k.append(end_pt_2)
			# print "Adding new edge endp2", end_pt_2
		random_VC_k = list(set(random_VC_k))
		print "current iteration VC length", len(random_VC_k)
	return most_optimal_VS_so_far or VC_obtained or random_VC_k




f = open("email.graph")
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


