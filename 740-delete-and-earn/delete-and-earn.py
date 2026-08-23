class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        observations: 
        - the ordering of the array does not matter 
        - picking the largest number need not necessarily give the maximum points 
        - if you pick a number pick all occurances of them i.e. pick = (freq * num)+ dfs(i + 1)
        - how do we test
        '''

        counter = collections.Counter(nums) 
        arr = []
        for item, freq in counter.items():
            arr.append((item, item * freq))
        arr.sort()

        @cache
        def dfs(i): 
            if i >= len(arr): 
                return 0
            
            pick = 0
            if (i + 1) < len(arr) and arr[i + 1][0] == arr[i][0] + 1:
                pick = arr[i][1] + dfs(i + 2)
            else: 
                pick = arr[i][1] + dfs(i + 1)
            skip = dfs(i + 1)
            return max(pick, skip)
        
        return dfs(0)

        