import os
import json

files = [file for file in os.listdir() if file.endswith('.txt') and os.path.isfile(file)]

graphs = {}
graphs_file = open('graphs.json', 'w')
graphs_file.write('{\n')

for i, file in enumerate(files):
    graph = {}
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines: 
            v, u = line.split()  
            v = int(v)
            u = int(u)
            if v != u:
                graph[str(v)] = graph.get(str(v), []) + [u]
                graph[str(u)] = graph.get(str(u), []) + [v]
    for v in graph:
        graph[v] = list(sorted(graph[v]))
    graphs[file] = graph
    print(f'Processed {i+1}/{len(files)} files, {file}')
    graphs_file.write(f'    "{file}": {json.dumps(graph, indent=4)}')
    if i < len(files) - 1:
        graphs_file.write(',')
    graphs_file.write('\n')
graphs_file.write('}')
graphs_file.close()