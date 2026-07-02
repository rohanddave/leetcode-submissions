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
        base case if j == len(p) return i == len(s)
        elif i == len(s) return false
        '''
        def can(k): 
            removable_subset = set(removable[:k + 1])
            def check(i, j): 
                if j == len(p):
                    return True
                elif i == len(s):
                    return False 
                
                if i in removable_subset: 
                    return check(i + 1, j)
                if s[i] == p[j]:
                    return check(i + 1, j + 1)
                return check(i + 1, j)
            return check(0, 0)

        left,  right = 0, len(removable)

        while left < right: 
            m = (left + right) // 2

            if not can(m):
                right = m
            else:
                left = m + 1
        return left

