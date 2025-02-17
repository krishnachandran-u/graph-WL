from src.graph import Graph
from bidict import bidict
from pprint import pprint
from copy import deepcopy

def VF2(g1: Graph, g2: Graph) -> bool:
    matched: bidict[int, int] = bidict() 
    unv1: list[int] = deepcopy(g1.vertices)
    unv2: list[int] = deepcopy(g2.vertices)

    def VF2Rec(matched: bidict[int, int], unv1: list[int], unv2: list[int]) -> bidict[int, int]:
        def isFeasible(v1: int, v2: int) -> bool: 
            for u1 in g1.neighbors(v1):
                if u1 in matched:
                    u2 = matched[u1]
                    if not g2.adjacent(v2, u2):
                        return False
            for u1 in g1.nonNeighbors(v1):
                if u1 in matched:
                    u2 = matched[u1]
                    if g2.adjacent(v2, u2):
                        return False
            for u2 in g2.neighbors(v2):
                if u2 in matched.inverse:
                    u1 = matched.inverse[u2]
                    if not g1.adjacent(v1, u1):
                        return False
            for u2 in g2.nonNeighbors(v2):
                if u2 in matched.inverse:
                    u1 = matched.inverse[u2]
                    if g1.adjacent(v1, u1):
                        return False
            return True

        if len(matched) == len(g1.vertices):
            return matched

        for v1 in unv1:
            for v2 in unv2:
                if isFeasible(v1, v2):
                    matched[v1] = v2
                    unv1.remove(v1)
                    unv2.remove(v2)
                    result = VF2Rec(matched, unv1, unv2)
                    if result is not None:
                        return result
                    matched.pop(v1)
                    unv1.append(v1)
                    unv2.append(v2)
        return None

    return VF2Rec(matched, unv1, unv2)