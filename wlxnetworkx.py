import networkx as nx
from src.WL1 import checkWL1
import sys
import json
from src.graph import Graph 
from pprint import pprint
import subprocess
import os

def check_isomorphism(graph1_json, graph2_json):
    G1 = nx.Graph(graph1_json)
    G2 = nx.Graph(graph2_json)
    
    return nx.is_isomorphic(G1, G2)

def wl1xnetworkx(filename):
    result = {
        "true positive": 0,
        "true negative": 0,
        "false positive": 0,
        "false negative": 0
    }
    with open(f'./data/{filename}', 'r') as f:
        data: dict = json.loads(f.read())
    for key in data:
        networkx_result = check_isomorphism(data[key], data[key])

        g0, g1 = Graph(filename, key), Graph(filename, key)
        WL1_result = checkWL1(g0, g1)

        if networkx_result and WL1_result:
            result["true positive"] += 1
        elif networkx_result and not WL1_result:
            result["false negative"] += 1
        elif not networkx_result and WL1_result:
            result["false positive"] += 1
        else:
            result["true negative"] += 1
    return result

if __name__ == "__main__":
    results = {}
    vertices_upper_bound = int(sys.argv[1])
    for i in range(1, vertices_upper_bound + 1):
        subprocess.run(['python', 'generateGraphs.py', str(i)])
        results[i] = wl1xnetworkx(f'graphs_{i}.json')
        os.remove(f'./data/graphs_{i}.json')
    with open(f'./result/wl1xnetworkx.json', 'w') as f:
        f.write(json.dumps(results, indent=2))

        