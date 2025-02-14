from src.graph import Graph
import time

def wl1(g: Graph, trace: bool = False) -> tuple[list[dict[int, int]], float] | tuple[dict[int, int], float]:
    start_time = time.perf_counter()

    colors_prev: dict[int, int] = {
        v: 0 for v in g.vertices
    }

    if trace: 
        colors_stack: list[dict[int, int]] = [colors_prev]

    msets_prev_occ: list[int] = [0]*len(g.vertices)

    while True: 
        colors_next: dict[int, int] = {}
        msets_next: dict[tuple[int], list[int]] = {}

        for v in g.vertices:
            mset_next: list[int] = [colors_prev[v]] 
            for u in g.neighbors(v):
                mset_next.append(colors_prev[u])
            mset_next = tuple(sorted(mset_next))
            msets_next[mset_next] = msets_next.get(mset_next, []) + [v] 
    
        for i, mset in enumerate(msets_next.keys()):
            for v in msets_next[mset]:
                colors_next[v] = i

        if trace: 
            colors_stack.append(colors_next)

        msets_next_occ = [len(v) for v in msets_next.values()]
        msets_next_occ.sort()

        if msets_prev_occ == msets_next_occ:
            break

        colors_prev = colors_next
        msets_prev_occ = msets_next_occ 

    end_time = time.perf_counter()
    exec_time = end_time - start_time

    if trace: 
        return colors_stack, msets_next_occ, exec_time
    else: 
        return colors_next, msets_next_occ, exec_time

def check_wl1(g1: Graph, g2: Graph) -> bool:
    _, msets_next_occ1, _ = wl1(g1)
    _, msets_next_occ2, _ = wl1(g2)

    return msets_next_occ1 == msets_next_occ2