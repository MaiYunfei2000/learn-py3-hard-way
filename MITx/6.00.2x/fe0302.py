class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
               
class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

# Consider our representation of permutations of students in a line from Exercise 1. (The teacher only swaps the positions of two students that are next to each other in line.) Let's consider a line of three students, Alice, Bob, and Carol (denoted A, B, and C). Using the Graph class created in the lecture, we can create a graph with the design chosen in Exercise 1: vertices represent permutations of the students in line; edges connect two permutations if one can be made into the other by swapping two adjacent students.

# We construct our graph by first adding the following nodes:

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

# debug use:
# while True:
#     try:
#         exec(input("play until you hit ctrl-D\n>>> "))
#     except:
#         pass

# Add the appropriate edges to the graph.

# 也许可以用于验证：
# 6个元素两两组合，用组合数算得15种组合，即15条双向联结。
# 喂泥垢了，不是自由组合啊！你还要排除不可能的组合，比如ABC<->CBA。
# 有6个元素，于是共有6种这种情况，于是共有15-6=9条双向联结？
# 还有呢，ABC<->BCA这种也是要交换两次！不对啊，再减6就是3了呀！
# 呜不算了，脑子还不如中学生……

############################################################

g.addEdge(Edge(g.getNode("ABC"), g.getNode("ACB")))
g.addEdge(Edge(g.getNode("ABC"), g.getNode("BAC")))
g.addEdge(Edge(g.getNode("ACB"), g.getNode("CAB")))
g.addEdge(Edge(g.getNode("BAC"), g.getNode("BCA")))
g.addEdge(Edge(g.getNode("BCA"), g.getNode("CBA")))
g.addEdge(Edge(g.getNode("CAB"), g.getNode("CBA")))

############################################################

print(g)