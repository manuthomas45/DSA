class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end_of_word=True
    # def search(self,word):#search for complete word
    #     node=self.root
    #     for char in word:
    #         if char not in node.children:
    #             return False
    #         node=node.children[char]
    #     return node.is_end_of_word
    def search(self, word, prefix_search=False):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True if prefix_search else node.is_end_of_word

trie=Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("james")
trie.insert("naveen")
trie.insert("anandh")
print(trie.search("ap",prefix_search=True))