from src.graph import Graph
from itertools import combinations_with_replacement
from time import perf_counter
from pprint import pprint

def checkWLk(g1: Graph, g2: Graph, k: int) -> bool:
    colors1, _= WLk(g1, k)
    colors2, _= WLk(g2, k)

    colors1Occ: dict = {}
    colors2Occ: dict = {}

    for color in colors1.values():
        colors1Occ[color] = colors1Occ.get(color, 0) + 1
    for color in colors2.values():
        colors2Occ[color] = colors2Occ.get(color, 0) + 1

    for color, occ in colors1Occ.items():
        if occ != colors2Occ.get(color, 0):
            return False
    
    for color, occ in colors2Occ.items():
        if occ != colors1Occ.get(color, 0):
            return False

    return True

def WLk(g: Graph, k: int, trace: bool = False) -> tuple[list[dict[tuple[int], int]], list[int], float] | tuple[dict[tuple[int], int], list[int], float]:
    if not 1 <= k <= len(g.vertices):
        raise ValueError('1 <= k <= |V| must hold')

    startTime = perf_counter()

    kTuples: set[tuple[int]] = set()
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

    colorsPrevEnum: dict[int, int] = {color: i for i, color in enumerate(list(dict.fromkeys(colorsPrev.values())))}
    colorsPrev = {t: colorsPrevEnum[colorsPrev[t]] for t in kTuples}

    if trace:
        colorsStack = [colorsPrev]

    while True:
        colorsNext: dict[tuple[int], int] = dict() 

        for t in kTuples:
            colorNextT: list[tuple[int]] = [(colorsPrev[t],)]
            for i, v in enumerate(t):
                colorNextV: list[int] = []
                for u in g.neighbors(v):
                    colorNextV.append(colorsPrev[tuple(sorted(t[:i] + (u,) + t[i+1:]))])
                colorNextT.append(tuple(sorted(colorNextV)))
            colorsNext[t] = hash(tuple(sorted(colorNextT)))

        colorsNextEnum: dict[int, int] = {color: i for i, color in enumerate(list(dict.fromkeys(colorsNext.values())))}
        colorsNext = {t: colorsNextEnum[colorsNext[t]] for t in kTuples}

        if trace:
            colorsStack.append(colorsNext)

        if colorsNext == colorsPrev:
            break

        colorsPrev = colorsNext

    endTime = perf_counter()
    execTime = endTime - startTime

    if trace:
        return colorsStack, execTime
    else:
        return colorsNext, execTime