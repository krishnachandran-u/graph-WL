from src.graph import Graph
from src.naive import naive 

if __name__ == "__main__":
    g0 = Graph('test.json', 'test0')
    g1 = Graph('test.json', 'test0iso')

    is_isomorphic, execTime = naive(g0, g1)

    if is_isomorphic:
        print("Isomorphic")
    else:
        print("Not isomorphic")
    