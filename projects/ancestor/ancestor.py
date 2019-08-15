class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            print("WARNING: vertex does exist")

    def add_edge(self, parent, child):
        """
        Add a directed edge to the graph.
        """
        if parent not in self.vertices or child not in self.vertices:
            print("WARNING: vertex does not exist")
        else:
            self.vertices[child].add(parent)


def earliest_ancestor(dataset, starting_node):
    graph = Graph()

    hash = set()
    for data in dataset:
        for i in data:
            if i not in hash:
                hash.add(i)

    # print(hash)
    for key in hash:
        graph.add_vertex(key)

    for data in dataset:
        graph.add_edge(data[0], data[1])

    if len(graph.vertices[starting_node]) == 0:
        return -1

    def dft(starting_node):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        path = {}
        visited = []
        stack = Stack()
        stack.push(starting_node)
        while stack.size() > 0:
            node = stack.pop()

            if node not in visited:
                visited.append(node)
                # print(node)
                parents = graph.vertices[node]
                # print(parents)
                if len(parents) == 0:
                    path[len(visited)] = list(visited)

                    found = False
                    while not found:

                        if len(visited) <= 1:
                            break

                        last_visited = visited[-1]
                        parents = graph.vertices[last_visited]

                        if len(parents) == 0:

                            visited.pop()
                            last_visited = visited[-1]
                        else:
                            for parent in parents:
                                if parent in stack.stack:
                                    found = True
                                    break
                            if not found:
                                visited.pop()
                else:
                    nums = []
                    for parent in graph.vertices[node]:
                        # if largest is None or largest < parents:
                        #     largest = parents
                        nums.append(parent)
                    if len(nums) > 1:
                        nums.sort()
                    if len(nums) > 0:
                        for num in nums:
                            stack.push(num)
        biggest = None
        for key in path:
            if biggest == None or biggest <= key:
                biggest = key

        return path[biggest][-1]

    return dft(starting_node)


print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                         (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 11))

# [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
