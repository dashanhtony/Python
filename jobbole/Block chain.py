import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        print(sha)
        sha.update(str(self.index).encode("utf8") +
                   str(self.timestamp).encode("utf8") +
                   str(self.data).encode("utf8") +
                   str(self.previous_hash).encode("utf8"))
        return sha.hexdigest()

a=Block(1,2222,33333,444444444)
a.hash
print(a.hash)