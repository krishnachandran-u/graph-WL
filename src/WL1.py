from src.graph import Graph
import time

def checkWL1(g1: Graph, g2: Graph) -> bool:
    colors1, _ = WL1(g1)
    colors2, _ = WL1(g2)

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

def WL1(g: Graph, trace: bool = False) -> tuple[list[dict[int, int]], float] | tuple[dict[int, int], float]:
    startTime = time.perf_counter()

    colorsPrev: dict[int, int] = {v: len(g.neighbors(v)) for v in g.vertices}
    colorsPrevEnum: dict[int, int] = {color: i for i, color in enumerate(list(dict.fromkeys(colorsPrev.values())))}
    colorsPrev = {v: colorsPrevEnum[colorsPrev[v]] for v in g.vertices}

    if trace:
        colorsStack = [colorsPrev]

    while True: 
        colorsNext: dict[int, int] = {}

        for v in g.vertices:
            colorNextV: list[int] = [] 
            for u in g.neighbors(v):
                colorNextV.append(colorsPrev[u])
            colorNextV = tuple(sorted(colorNextV))
            colorsNext[v] = hash(colorNextV)

        colorsNextEnum: dict[int, int] = {color: i for i, color in enumerate(list(dict.fromkeys(colorsNext.values())))}
        colorsNext = {v: colorsNextEnum[colorsNext[v]] for v in g.vertices}
        
        if trace:
            colorsStack.append(colorsNext)
    
        if colorsNext == colorsPrev:
            break

        colorsPrev = colorsNext

    endTime = time.perf_counter()
    execTime = endTime - startTime
        
    if trace:
        return colorsStack, execTime
    else:
        return colorsNext, execTime