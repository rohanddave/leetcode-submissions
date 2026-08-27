class TrieNode: 
    def __init__(self, val=''): 
        self.val = val 
        self.children = {}
        self.end = None

class Trie: 
    def __init__(self): 
        self.root = TrieNode()    

    def insert(self, word): 
        curr = self.root 
        for char in word: 
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.end = word 
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        trie = Trie()
        for word in words: 
            trie.insert(word) 
        
        res = []
        def dfs(r, c, node): 
            if node.end:
                res.append(node.end)
                node.end = None
            
            tmp = board[r][c]
            board[r][c] = '#'
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in node.children: 
                    dfs(nr, nc, node.children[board[nr][nc]])
            board[r][c] = tmp

        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in trie.root.children:
                    dfs(i, j, trie.root.children[char])
        return res