class DistributedDatabase:
    def __init__(self):
        self.nodes = []
        self.lock = threading.Lock()

    def add_node(self, node):
        with self.lock:
            self.nodes.append(node)

    def write_data(self, data):
        # Assuming consensus is required for writing data
        for node in self.nodes:
            node.commit(data)  # Mock function for writing data
