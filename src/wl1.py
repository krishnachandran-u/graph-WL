from src.graph import Graph
from multiset import * 
import time

def wl1(g: Graph, trace: bool = False) -> tuple[list[dict[int, int]], float] | tuple[dict[int, int], float]:
    start_time = time.perf_counter()

    colors_prev: dict[int, int] = {
        v: 0 for v in g.vertices
    }

    if trace: 
        colors_stack: list[dict[int, int]] = [colors_prev]

    msets_prev_occ: Multiset = Multiset([0]*len(g.vertices))

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

        if trace: 
            colors_stack.append(colors_next)

        msets_next_occ = Multiset([len(v) for v in msets_next.values()])

        if msets_next_occ == msets_prev_occ:
            break

        colors_prev = colors_next
        msets_prev_occ = msets_next_occ

    end_time = time.perf_counter()
    exec_time = end_time - start_time

    if trace: 
        return colors_stack, exec_time
    else: 
        return colors_next, exec_time