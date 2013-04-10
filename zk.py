import zookeeper


class ZooKeeperConnection:
    def __init__(self, host, root = "/"):
        self.handle = zookeeper.init(host)
        self.root = root

    def disconnect(self):
        zookeeper.close(self.handle)

    def children(self, path):
        p = self.root + path
        return zookeeper.get_children(self.handle, p)

    def raw_data(self, path):
        return zookeeper.get(self.handle, self.root + path, None)

    def set(self, path, data):
        return zookeeper.set(self.handle, self.root + path, data)

    def delete(self, path):
        return zookeeper.delete(self.handle, self.root + path)
