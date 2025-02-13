from src.graph import Graph
from multiset import * 

def wl_1(g: Graph) -> list[dict[int, int]]:
    colors_prev: dict[int, int] = {
        v: 0 for v in g.vertices
    }

    colors_stack: list[dict[int, int]] = [colors_prev]

    msets_prev_occ = Multiset([0]*len(g.vertices))

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

        colors_stack.append(colors_next)

        msets_next_occ = Multiset([len(v) for v in msets_next.values()])

        if msets_next_occ == msets_prev_occ:
            break

        colors_prev = colors_next
        msets_prev_occ = msets_next_occ

    return colors_stack