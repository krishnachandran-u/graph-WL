from src.graph import Graph
from itertools import combinations_with_replacement
from time import perf_counter

def WLk(g: Graph, k: int, trace: bool = False) -> tuple[list[dict[tuple[int], int]], list[int], float] | tuple[dict[tuple[int], int], list[int], float]:
    if not 1 <= k <= len(g.vertices):
        raise ValueError('1 <= k <= |V| must hold')

    startTime = perf_counter()

    kTuples: set[tuple[int]] = [] 
    for comb in combinations_with_replacement(g.vertices, k):
        kTuples.add(comb)

    colorsPrev: dict[tuple[int], int] = dict()
    for t in kTuples:
        colorPrevT: list[int] = [] 
        for i in range(len(t)):
            for j in range(i+1, len(t)):
                if t[j] == t[i]:
                    colorPrevT.append(0)
                elif t[j] in g.neighbors(t[i]):
                    colorPrevT.append(1)
                else:
                    colorPrevT.append(2)
        colorsPrev[t] = hash(tuple(sorted(colorPrevT)))

    if trace:
        colorsStack = [colorsPrev]

    colorsPrevHash: dict[int, int] = dict()
    for color in colorsPrev.values():
        colorsPrevHash[color] = colorsPrevHash.get(color, 0) + 1

    colorsPrevOcc: list[int] = sorted(list(colorsPrevHash.values()))

    while True:
        colorsNext: dict[tuple[int], int] = dict() 
        colorsNextHash: dict[int, int] = dict()

        for t in kTuples:
            colorNextT: list[int] = [colorsPrev[t]]
            for i, v in enumerate(t):
                colorNextV: list[int] = []
                for u in g.neighbors(v):
                    if u in t:
                        colorNextV.append(colorsPrev[sorted(t[:i] + (u,) + t[i+1:])])
                colorNextT.append(tuple(sorted(colorNextV)))
            colorsNext[t] = hash(tuple(sorted(colorNextT)))
            colorsNextHash[colorsNext[t]] = colorsNextHash.get(colorsNext[t], 0) + 1

        colorsNextOcc: list[int] = sorted(list(colorsNextHash.values()))

        if trace:
            colorsStack.append(colorsNext)

        if colorsNextOcc == colorsPrevOcc:
            break

        colorsPrev = colorsNext
        colorsPrevOcc = colorsNextOcc

        endTime = perf_counter()
        execTime = endTime - startTime

        if trace:
            return colorsStack, colorsNextOcc, execTime
        else:
            return colorsNext, colorsNextOcc, execTime