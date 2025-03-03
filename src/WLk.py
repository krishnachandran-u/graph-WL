import copy
import pprint
import itertools
import hashlib
import networkx as nx
from collections import Counter

def convertJsonToNetworkx(graphJson):
    G = nx.Graph()
    for node in graphJson:
        G.add_node(int(node))
    for node, neighbors in graphJson.items():
        node = int(node)
        for neighbor in neighbors:
            neighbor = int(neighbor)
            if not G.has_edge(node, neighbor):
                G.add_edge(node, neighbor)
    return G

def baseWL(G_, k, verbose, nSet, initialColorsFunc, findNeighborsFunc):    
    if verbose:
        print('-----------------------------------')
        print('Starting the execution for the graph')
    
    G, n = nSet(G_)
    colors = initialColorsFunc(n)
    oldColors = copy.deepcopy(colors)
    if verbose:
        print(f'Initial Color hashes: \n {colors} \n')
    for i in range(len(n)):
        for node in n:
            neighColors = "".join([colors[i][0] for i in findNeighborsFunc(G, n, node)])
            colors[node].extend([neighColors])
            colors[node].sort()
        if verbose:
            print(f'Colors before hashes at iteration {i}: {colors} \n')
        colors = {i: [hashlib.sha224("".join(colors[i]).encode('utf-8')).hexdigest()] for i in colors}
        if verbose:
            print(f'Colors hashes at iteration {i}: \n {colors} \n')
            print(f'Histogram: \n {sorted(Counter([item for sublist in colors.values() for item in sublist]).items())} \n')
        if (list(Counter([item for sublist in colors.values() for item in sublist]).values()) == 
            list(Counter([item for sublist in oldColors.values() for item in sublist]).values())) and i != 0:
            if verbose:
                print(f'Converged at iteration {i}!')
            break
        oldColors = copy.deepcopy(colors)
    canonicalForm = sorted(Counter([item for sublist in colors.values() for item in sublist]).items())
    if verbose:
        print(f'Canonical Form Found: \n {canonicalForm} \n')
    return canonicalForm

def WL(G, k=2, verbose=False):
    def nSet(G):
        G = nx.convert_node_labels_to_integers(G)
        return G, list(G.nodes())
    def setInitialColors(n):
        return {i: [hashlib.sha224("1".encode('utf-8')).hexdigest()] for i in n}
    def findNeighbors(G, n, node):
        return G.neighbors(node)
    return baseWL(G, k, verbose, nSet, setInitialColors, findNeighbors)

def kWL(G, k, verbose=False):
    def nSet(G):
        G = nx.convert_node_labels_to_integers(G)
        V = list(G.nodes())
        Vk = [comb for comb in itertools.combinations(V, k)]
        return G, Vk
    def setInitialColors(n):
        return {i: [hashlib.sha224(str(i).encode('utf-8')).hexdigest()] for i in n}
    def findNeighbors(G, Vk, node):
        return [n for n in Vk if len(set(n) - set(node)) == 1]
    return baseWL(G, k, verbose, nSet, setInitialColors, findNeighbors)

def fkWL(G, k, verbose=False):
    def nSet(G):
        G = nx.convert_node_labels_to_integers(G)
        V = list(G.nodes())
        Vk = [comb for comb in itertools.product(V, repeat=k)]
        return G, Vk
    def setInitialColors(n):
        return {i: [hashlib.sha224(str(i).encode('utf-8')).hexdigest()] for i in n}
    def findNeighbors(G, Vk, node):
        V = list(G.nodes())
        vals = []
        for i in range(k):
            w = []
            nodesToAdd = [u for u in V if u != node[i]]
            for u in nodesToAdd:
                aux = list(node)
                aux[i] = u
                w.append(tuple(aux))
            vals.extend(w)
        return vals

    return baseWL(G, k, verbose, nSet, setInitialColors, findNeighbors)

def compareGraphs(G1Json, G2Json, method='WL', k=2, verbose=False):
    G1 = convertJsonToNetworkx(G1Json)
    G2 = convertJsonToNetworkx(G2Json)
    
    methods = {
        'WL': WL,
        'kWL': kWL,
        'fkWL': fkWL
    }

    if len(G1.nodes()) != len(G2.nodes()):
        if verbose:
            print('Non-Isomorphic by different number of nodes!')
        return False
    
    c1 = methods[method](G1, k, verbose)
    c2 = methods[method](G2, k, verbose)

    return c1 == c2