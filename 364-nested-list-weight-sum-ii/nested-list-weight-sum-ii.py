# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: list[NestedInteger]) -> int:
        max_depth = float('-inf')

        def get_max_depth(arr, depth): 
            nonlocal max_depth
            
            for j in range(len(arr)):
                if arr[j].isInteger():
                    max_depth = max(max_depth, depth)
                else:
                    get_max_depth(arr[j].getList(), depth + 1)
        
        res = 0
        def dfs(arr, depth): 
            nonlocal res, max_depth
            
            for j in range(len(arr)):
                if arr[j].isInteger():
                    weight = max_depth - depth + 1 
                    res += arr[j].getInteger() * weight
                else:
                    dfs(arr[j].getList(), depth + 1)
                
        get_max_depth(nestedList, 1)
        dfs(nestedList, 1)
        return res


        