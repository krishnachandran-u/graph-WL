from src.graph import Graph
from src.VF2 import VF2
from bidict import bidict
from pprint import pprint

if __name__ == "__main__":
    g0 = Graph('test.json', 'test0')
    g1 = Graph('test.json', 'test0iso')

    matched: bidict = VF2(g0, g1)

    if matched is not None:
        matchedDict = dict(matched)
        print("Isomorphic with mapping")
        pprint(matchedDict, width=1)
    else: 
        print("Not isomorphic")
