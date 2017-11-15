import networkx as nx

def MVC_approx(G):
    Gprime = G.copy()
    C = []
    while Gprime.edges():
        (u, v) = Gprime.edges()[0]
        C.append(u)
        C.append(v)
        for i in Gprime.neighbors(u):
            Gprime.remove_edge(u,i)
        for j in Gprime.neighbors(v):
            Gprime.remove_edge(v,j)

    return C

# maybe rewrite to find the edge with most neighbors?
