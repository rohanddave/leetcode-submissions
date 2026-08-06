class TrieNode: 
    def __init__(self, val=''):
        self.val = val
        self.is_end = False
        self.hot = []
        self.children = {}

class Trie: 
    def __init__(self): 
        self.root = TrieNode()
    
    def _insert(self, node, word, i, count):
        if i == len(word):
            node.is_end = True
            return 
        
        if word[i] not in node.children:
            node.children[word[i]] = TrieNode(word[i])
        
        child_node = node.children[word[i]]

        # Remove stale frequency for the same sentence

        child_node.hot = [
            (freq, sentence)
            for freq, sentence in child_node.hot
            if sentence != word
        ]
        child_node.hot.append((count, word))
        child_node.hot.sort(key=lambda x: (-x[0], x[1]))

        if len(child_node.hot) > 3:
            child_node.hot.pop()
        
        self._insert(child_node, word, i + 1, count)
        return
        
        
    def insert(self, word, count): 
        self._insert(self.root, word, 0, count)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.freqs = collections.defaultdict(int)
        for i in range(len(sentences)): 
            self.trie.insert(sentences[i], times[i])
            self.freqs[sentences[i]] = times[i]
        self.curr = self.trie.root   
        self.curr_sentence = []

    def input(self, c: str) -> List[str]:
        if c == '#':
            sentence = ''.join(self.curr_sentence)
            self.freqs[sentence] += 1
            self.trie.insert(sentence, self.freqs[sentence])
            # reset 
            self.curr_sentence = []
            self.curr = self.trie.root
            return []
        
        self.curr_sentence.append(c)

        if self.curr:
            self.curr = self.curr.children[c] if c in self.curr.children else None
        
        if self.curr:
            return [suggestion for _, suggestion in self.curr.hot]
        return []

        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)    