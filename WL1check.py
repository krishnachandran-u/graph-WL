from src.graph import Graph
from src.WL1 import checkWL1

if __name__ == "__main__":
    g0 = Graph('test.json', 'test0')
    g1 = Graph('test.json', 'test1')

    if checkWL1(g0, g1):
        print('Same color classes')
    else:
        print('Different color classes')
