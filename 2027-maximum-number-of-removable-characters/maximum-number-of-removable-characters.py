class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        '''
        p is a subsequence of s 
        removable = subset of indices of s 

        choose k:
        - removing first k indices in removable p is still a subsequece of s

        goal: return max k such that p is still a subsequence of s 

        observations: 
        - subsequence of a string is when some or none character deleted without changing the order of remaining characters 
        - answer lies in the range [0, len(removable)]

        example: 
        Input: s = "abcacb", p = "ab", removable = [3,1,0]
        Output: 2

        when k = 3
        indices to remove from s = [3, 1, 0]
        s => ccb

        when k = 2
        removable = [3, 1]
        s => accb

        approach: 
        - since the answer lies in a known space [0, len(removable)] we can use binary search on this space where we want to look for the maximum value of k. 
        - can(k) will create a set of [0:k] of removable and perform a string subsequence check between s and p where if i is in the subset of removable we skip that character else we perform subsequence check: 
            - if s[i] == p[j] return dfs(i + 1, j + 1) 
            - else return dfs(i + 1, j)
        base case if j == len(p) return True
        elif i == len(s) return false

        Complexity: 
        TC: O(log len(removable) * len(p))
        '''
        def can(k): 
            removable_subset = set(removable[:k])
            j = 0
            for i in range(len(s)): 
                if j == len(p):
                    break
                if i in removable_subset or s[i] != p[j]:
                    continue 
                j += 1
            return j == len(p)

        left,  right = 0, len(removable) + 1

        while left < right: 
            m = (left + right) // 2

            if not can(m):
                right = m
            else:
                left = m + 1
        return left - 1

