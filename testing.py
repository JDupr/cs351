from graph import Graph

def init_graph(fname):
    with open(fname) as f:
        lines = f.readlines()

    graph = Graph()

    for line in lines:
        [parent, child] = line.strip().split('%')
        graph.add_edge(parent, child)

    graph.sort_nodes()

    return graph

if __name__ == "__main__":
    graph_object = init_graph('edges.txt')
    graph_object.display()
    for i in range(10000):
        for node in graph_object.nodes:
            node.update_pagerank(0.15, len(graph_object.nodes))
        graph_object.normalize_pagerank()
    arr = graph_object.get_pagerank_list()
    with open('graph.txt', 'w+') as file:
        file.write(str(arr))