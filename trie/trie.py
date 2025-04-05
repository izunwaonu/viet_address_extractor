

from .trie_node import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a word into the trie."""
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.value = word

    def search_longest(self, text):
        """Finds the longest matching word from anywhere in the text."""
        text = text.lower()
        longest_match = ""
        
        for start in range(len(text)):
            node = self.root
            match = ""
            
            for i in range(start, len(text)):
                char = text[i]
                
                if char not in node.children:
                    break
                
                node = node.children[char]
                match += char
                
                if node.is_end:
                    longest_match = node.value if len(node.value) > len(longest_match) else longest_match
        
        return longest_match
