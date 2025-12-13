"""
Implement Trie (Prefix Tree) - LeetCode #208
Frequency: 70% (Common - System design)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
store and retrieve keys in a dataset of strings.

Time Complexity: O(m) for insert/search/prefix where m is key length
Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of keys, M is average length
"""

from typing import Optional, Dict, List


class TrieNode:
    """Node in a Trie"""
    
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie (Prefix Tree) implementation
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert a word into the trie"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search for a word in the trie"""
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """Check if any word in the trie starts with the given prefix"""
        node = self._find_node(prefix)
        return node is not None
    
    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        """Find node corresponding to prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node
    
    def get_all_words_with_prefix(self, prefix: str) -> List[str]:
        """Get all words that start with the given prefix"""
        node = self._find_node(prefix)
        if not node:
            return []
        
        words = []
        self._dfs(node, prefix, words)
        return words
    
    def _dfs(self, node: TrieNode, current_word: str, words: List[str]) -> None:
        """DFS to find all words from a node"""
        if node.is_end_of_word:
            words.append(current_word)
        
        for char, child_node in node.children.items():
            self._dfs(child_node, current_word + char, words)


class WordDictionary:
    """
    Add and Search Words - LeetCode #211
    Design a data structure that supports adding new words and finding 
    if a string matches any previously added string (with '.' wildcard)
    """
    
    def __init__(self):
        self.trie = Trie()
    
    def add_word(self, word: str) -> None:
        """Add word to dictionary"""
        self.trie.insert(word)
    
    def search(self, word: str) -> bool:
        """Search word (supports '.' as wildcard)"""
        return self._search_helper(self.trie.root, word, 0)
    
    def _search_helper(self, node: TrieNode, word: str, index: int) -> bool:
        """Helper for wildcard search"""
        if index == len(word):
            return node.is_end_of_word
        
        char = word[index]
        
        if char == '.':
            # Try all children
            for child_node in node.children.values():
                if self._search_helper(child_node, word, index + 1):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self._search_helper(node.children[char], word, index + 1)


# Test cases
if __name__ == "__main__":
    # Test Trie
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")
    
    print(f"Search 'app': {trie.search('app')}")  # True
    print(f"Search 'appl': {trie.search('appl')}")  # False
    print(f"Starts with 'app': {trie.starts_with('app')}")  # True
    print(f"Words with prefix 'app': {trie.get_all_words_with_prefix('app')}")
    
    # Test Word Dictionary
    word_dict = WordDictionary()
    word_dict.add_word("bad")
    word_dict.add_word("dad")
    word_dict.add_word("mad")
    
    print(f"\nSearch 'pad': {word_dict.search('pad')}")  # False
    print(f"Search 'bad': {word_dict.search('bad')}")  # True
    print(f"Search '.ad': {word_dict.search('.ad')}")  # True
    print(f"Search 'b..': {word_dict.search('b..')}")  # True

