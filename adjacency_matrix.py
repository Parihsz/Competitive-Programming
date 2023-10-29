#2d list implementation
class adjacency_matrix_1:
    def __init__(self, N):
        self.matrix = [[False for _ in range(N)] * N]
    def connect(self, a, b, bidirectional=True):
        self.matrix[a][b] = True
        if bidirectional:
            self.matrix[b][a] = True
    def is_connected(self, a, b):
        return self.matrix[a][b]

# adjacency matrix dictionary
class adjacency_matrix_1:
    def __init__(self, N):
        self.matrix = set()
    def connect(self, a, b, bidirectional=True):
        self.matrix.add((a, b))
        if bidirectional:
            self.matrix.add((b, a))
    def is_connected(self, a, b):
        return (a, b) in self.matrix
    