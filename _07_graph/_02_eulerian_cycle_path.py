class Graph:
    adjList = {}
    bidir = True

    def __init__(self, bidir=True):
        self.bidir = bidir
        pass
    def add_edge(self, start, end):
        self.adjList.setdefault(start, set()).add(end)
        if self.bidir:
            self.adjList.setdefault(end, set()).add(start)

    def has_eulerian_cycle(self):
        odd = 0
        for vertex in self.adjList:
            if len(self.adjList[vertex]) %2 == 1:
                odd += 1
        if odd == 0:
            return True
        else:
            return False

    def has_eulerian_path(self):
        odd = 0
        for vertex in self.adjList:
            if len(self.adjList[vertex]) % 2 == 1:
                odd +=1
        if odd == 0 or odd == 2:
            return True
        else:
            return False
    def print_adj_list(self):
        print(self.adjList)

def test():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 1)

    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    graph.add_edge(3, 6)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)

    graph.print_adj_list()
    print("eulerian cycle: ", graph.has_eulerian_cycle())
    print("eulerian path: ", graph.has_eulerian_path())





