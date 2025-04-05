# Basic TrieNode structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.value = None
