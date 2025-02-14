from src.graph import Graph

if __name__ == "__main__":
    g = Graph('test.json', 'test0')
    g.draw(save=True)