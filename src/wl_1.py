from src.graph import Graph
from multiset import * 

def wl_1(g: Graph):
    colors_prev: dict[int, int] = {v: 0 for v in g.vertices}

    while True: 
        colors_next: dict[int, int] = {}
        msets_next: dict[Multiset, list[int]] = {}

        for v in g.vertices:
            mset_next = Multiset()
            for u in g.neighbors(v):
                mset_next.add(colors_prev[u])
            msets_next[mset_next] = msets_next.get(mset_next, []) + [v] 
    
        for i, mset in enumerate(msets_next.keys()):
            for v in msets_next[mset]:
                colors_next[v] = i

        colors_prev_occurrence = Multiset(colors_prev.values())
        colors_next_occurrence = Multiset(colors_next.values())

        if colors_prev_occurrence == colors_next_occurrence:
            break

        colors_prev = colors_next

    return colors_next