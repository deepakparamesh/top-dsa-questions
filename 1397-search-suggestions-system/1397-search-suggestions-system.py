class TrieNode:
    def __init__(self):
        self.children = {}
        self.products = []  # Store products that pass through this node

class Solution:
    def suggestedProducts(self, products, searchWord):
        """
        Return suggestions for each prefix of searchWord using Trie approach.
        """
        # Build Trie
        root = self.buildTrie(products)
        
        result = []
        current_node = root
        
        # Process each character in searchWord
        for char in searchWord:
            if current_node and char in current_node.children:
                current_node = current_node.children[char]
                # Get up to 3 suggestions from current node
                suggestions = current_node.products[:3]
                result.append(suggestions)
            else:
                # No more matches possible for this and subsequent prefixes
                current_node = None
                result.append([])
        
        return result
    
    def buildTrie(self, products):
        """
        Build a trie with products sorted at each node.
        """
        # Sort products first to maintain lexicographical order
        products.sort()
        
        root = TrieNode()
        
        for product in products:
            node = root
            # Insert product character by character
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                # Add product to current node's list (already sorted due to pre-sorting)
                node.products.append(product)
        
        return root
        