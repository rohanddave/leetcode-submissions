class UnionFind: 
    def __init__(self, n): 
        self.size = [1] * n 
        self.parent = list(range(n))
        self.components = n
    
    def find(self, x): 
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y) 
        if px == py:
            return False
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        self.components -= 1
        return True 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)

        email_to_group = {}
        for group, accs in enumerate(accounts):
            for i in range(1, len(accs)):
                email = accs[i]
                if email in email_to_group: 
                    uf.union(email_to_group[email], group)

                email_to_group[email] = group

        res = []
        root_to_emails = collections.defaultdict(list)
        for email, group in email_to_group.items(): 
            root_to_emails[uf.find(group)].append(email)

        print(root_to_emails)
        for root, emails in root_to_emails.items():
            res.append([accounts[root][0]] + sorted(emails))
        return res

        