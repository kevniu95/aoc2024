def getInput(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

class GraphNode():
    def __init__(self, key: str, neighbors: list= None):
        self.key = key
        if not neighbors:
            self.neighbors = []

    def __str__(self) -> str:
        return f"Key: {self.key}, neighbors: {[i.key for i in self.neighbors]}"
    
    def __repr__(self) -> str:
        return f"Key: {self.key}, neighbors: {[i.key for i in self.neighbors]}"

def processInput(inputArray: list[str]) -> tuple[list[list[int]], list[int]]:
    nodes: dict[str, GraphNode] = {}
    for line in inputArray:
        letters = line.strip().split('-')
        graphNode = nodes.get(letters[0], GraphNode(letters[0]))
        neighbor = nodes.get(letters[1], GraphNode(letters[1]))
        graphNode.neighbors.append(neighbor)
        neighbor.neighbors.append(graphNode)
        nodes[letters[0]] = graphNode
        nodes[letters[1]] = neighbor
    return nodes

def visitNeighbors(node: GraphNode, 
                   cycles: set[tuple[int, int, int]]):
    for neighbor in node.neighbors:
        for node1 in node.neighbors:
            for node2 in neighbor.neighbors:
                if node1 == node2:
                    entry = [node.key, neighbor.key, node1.key]
                    entry.sort()
                    tup = tuple(entry)
                    if tup not in cycles:
                        cycles.add(tup)
    return
        

if __name__ == '__main__':
    inputArray = getInput('./day23/input1.txt')
    nodes = processInput(inputArray)
    
    cycles: set[tuple[int, int, int]] = set()
    for key, node in nodes.items():
        visitNeighbors(node, cycles)
    
    finalCycles = set()
    for cycle in cycles:
        for entry in cycle:
            if entry.startswith('t'):
                finalCycles.add(cycle)
    print(finalCycles)
    print(len(finalCycles))