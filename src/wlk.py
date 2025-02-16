from src.graph import Graph
from itertools import combinations_with_replacement

def wlk(g: Graph, k: int):
    kTuples = [] 
    for comb in combinations_with_replacement(g.vertices, k):
        kTuples.append(comb)
    colorsPrev: dict[tuple[int], set] = dict()
    for t in kTuples:
        tSet: set[int] = set()
        for i in range(len(t)):
            for j in range(i+1, len(t)):
                if t[j] == t[i]:
                    tSet.add(0)
                elif t[j] in g.neighbors(t[i]):
                    tSet.add(1)
                else:
                    tSet.add(2)
        colorsPrev[t] = hash(frozenset(tSet))