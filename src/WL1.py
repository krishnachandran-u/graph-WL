from src.graph import Graph
import time

def checkWL1(g1: Graph, g2: Graph) -> bool:
    _, colorsNextOcc1, _ = WL1(g1)
    _, colorsNextOcc2, _ = WL1(g2)

    return colorsNextOcc1 == colorsNextOcc2 

def WL1(g: Graph, trace: bool = False) -> tuple[list[dict[int, int]], list[int], float] | tuple[dict[int, int], list[int], float]:
    startTime = time.perf_counter()

    colorsPrev: dict[int, int] = {v: len(g.neighbors(v)) for v in g.vertices}

    if trace:
        colorsStack = [colorsPrev]

    colorsPrevHash: dict[int, int] = {} 
    for v, color in colorsPrev.items():
        colorsPrevHash[color] = colorsPrevHash.get(color, 0) + 1

    colorsPrevOcc: list[int] = sorted(list(colorsPrevHash.values()))

    while True: 
        colorsNext: dict[int, int] = {}
        colorsNextHash: dict[int, int] = {}

        for v in g.vertices:
            colorNextV: list[int] = [] 
            for u in g.neighbors(v):
                colorNextV.append(colorsPrev[u])
            colorNextV = tuple(sorted(colorNextV))
            colorsNext[v] = hash(colorNextV)
            colorsNextHash[colorsNext[v]] = colorsNextHash.get(colorsNext[v], 0) + 1

        colorsNextOcc: list[int] = sorted(list(colorsNextHash.values()))
        
        if trace:
            colorsStack.append(colorsNext)

        if colorsNextOcc == colorsPrevOcc:
            break
    
        colorsPrev = colorsNext
        colorsPrevOcc = colorsNextOcc

        endTime = time.perf_counter()
        execTime = endTime - startTime
        
        if trace:
            return colorsStack, colorsNextOcc, execTime
        else:
            return colorsNext, colorsNextOcc, execTime