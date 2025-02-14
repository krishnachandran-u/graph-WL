from src.graph import Graph
from src.wl1 import check_wl1

if __name__ == "__main__":
    g0 = Graph('test.json', 'test0')
    g1 = Graph('test.json', 'test1')

    if check_wl1(g0, g1):
        print('Same color classes')
    else:
        print('Different color classes')
