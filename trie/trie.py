

# from .trie_node import TrieNode

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         """Inserts a word into the trie."""
#         node = self.root
#         for char in word.lower():
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end = True
#         node.value = word

#     def search_longest(self, text):
#         """Finds the longest matching word from anywhere in the text."""
#         text = text.lower()
#         longest_match = ""
        
#         for start in range(len(text)):
#             node = self.root
#             match = ""
            
#             for i in range(start, len(text)):
#                 char = text[i]
                
#                 if char not in node.children:
#                     break
                
#                 node = node.children[char]
#                 match += char
                
#                 if node.is_end:
#                     longest_match = node.value if len(node.value) > len(longest_match) else longest_match
        
#         return longest_match

from .trie_node import TrieNode
import re

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

    def search_all_longest(self, text):
        """
        Returns a list of all non-overlapping longest matches in the text.
        Each match is a tuple: (start_index, end_index, matched_value)
        """
        text = text.lower()
        matches = []
        i = 0

        while i < len(text):
            node = self.root
            longest = ""
            longest_end = -1
            j = i

            while j < len(text):
                char = text[j]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_end:
                    longest = node.value
                    longest_end = j
                j += 1

            if longest:
                matches.append((i, longest_end, longest))
                i = longest_end + 1  # Move to next char after the match
            else:
                i += 1  # No match here, move one char forward

        return matches

    def search_longest(self, text):
        """
        Returns the longest single match found in the text.
        This is kept for backward compatibility.
        """
        matches = self.search_all_longest(text)
        return max(matches, key=lambda x: len(x[2]))[2] if matches else ""
